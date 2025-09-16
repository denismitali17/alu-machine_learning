#!/usr/bin/env python3
""" Variational Autoencoder """

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    Function that creates a variational autoencoder.

    Args:
        input_dims: integer containing the dimensions of the model input
        hidden_layers: list containing the number of nodes for each hidden
                       layer in the encoder, respectively
        latent_dims: integer containing the dimensions of the latent space
                     representation

    Returns:
        encoder, decoder, auto
    """

    # ----- Encoder -----
    X_input = keras.Input(shape=(input_dims,))
    Y_prev = keras.layers.Dense(
        units=hidden_layers[0], activation='relu'
    )(X_input)
    for i in range(1, len(hidden_layers)):
        Y_prev = keras.layers.Dense(
            units=hidden_layers[i], activation='relu'
        )(Y_prev)

    z_mean = keras.layers.Dense(units=latent_dims, activation=None)(Y_prev)
    z_log_sigma = keras.layers.Dense(units=latent_dims, activation=None)(Y_prev)

    def sampling(args):
        """Sampling from the latent space"""
        z_m, z_log_var = args
        batch = keras.backend.shape(z_m)[0]
        dim = keras.backend.int_shape(z_m)[1]
        epsilon = keras.backend.random_normal(shape=(batch, dim))
        return z_m + keras.backend.exp(0.5 * z_log_var) * epsilon

    z = keras.layers.Lambda(
        sampling,
        output_shape=(latent_dims,)
    )([z_mean, z_log_sigma])
    encoder = keras.Model(X_input, [z, z_mean, z_log_sigma])

    # ----- Decoder -----
    X_decode = keras.Input(shape=(latent_dims,))
    Y_prev = keras.layers.Dense(
        units=hidden_layers[-1], activation='relu'
    )(X_decode)
    for j in range(len(hidden_layers) - 2, -1, -1):
        Y_prev = keras.layers.Dense(
            units=hidden_layers[j], activation='relu'
        )(Y_prev)
    output = keras.layers.Dense(units=input_dims, activation='sigmoid')(Y_prev)
    decoder = keras.Model(X_decode, output)

    # ----- Autoencoder -----
    z_sample = encoder(X_input)[0]
    d_output = decoder(z_sample)
    auto = keras.Model(X_input, d_output)

    # ----- Loss Function -----
    def vae_loss(x, x_decoder_mean):
        # Reconstruction loss
        x_loss = keras.backend.sum(
            keras.backend.binary_crossentropy(x, x_decoder_mean),
            axis=1
        )
        # KL divergence loss
        kl_loss = -0.5 * keras.backend.sum(
            1 + z_log_sigma - keras.backend.square(z_mean)
            - keras.backend.exp(z_log_sigma),
            axis=1
        )
        return x_loss + kl_loss

    auto.compile(loss=vae_loss, optimizer='adam')
    return encoder, decoder, auto
