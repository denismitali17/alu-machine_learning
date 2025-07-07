## Convolutions and Pooling

## Project Description

This project implements foundational components of Convolutional Neural Networks (CNNs) using only Python and NumPy. It focuses on performing low-level image operations like convolution, padding, and pooling without any external deep learning libraries.

## Learning Objectives

By the end of this project, you should be able to explain:

- What is a convolution?
- What is a kernel/filter?
- What is padding? What’s the difference between “same” and “valid” padding?
- What is a stride?
- What are channels?
- What is max pooling? average pooling?
- How to perform a convolution over an image
- How to perform max/average pooling over an image

## Resources

Read/watch:
- Image Kernels
- Understanding Convolutional Layers
- A Comprehensive Guide to CNNs – the ELI5 Way
- What is max pooling?
- Edge Detection Examples
- Padding, Strided Convolutions
- Convolutions over Volumes, Pooling Layers
- Implementing ‘SAME’ and ‘VALID’ padding in Python  
  Note: Use `floor` rounding for valid padding (not `ceil`)

Skim:
- Convolution
- Kernel (image processing)

References:
- numpy.pad
- A Guide to Convolution Arithmetic for Deep Learning

## Requirements

- Python 3.5
- NumPy 1.15 only
- No use of `np.convolve`
- Only allowed imports:
  ```python
  import numpy as np
  from math import ceil, floor
  ```
- Files must:
  - Be executable
  - Start with `#!/usr/bin/env python3`
  - End with a newline
  - Pass `pycodestyle` (v2.5)
  - Include docstrings for all modules, classes, and functions

## Project Files

- Convolution implementation
- Padding logic
- Stride handling
- Max and average pooling
- Multi-channel image support

## Dataset

Please download the required dataset for testing (link to be provided by instructor or project guide).

## Testing

Run:
```bash
wc -l filename.py
python3 -c 'print(__import__("your_module").__doc__)'
python3 -c 'print(__import__("your_module").YourClass.__doc__)'
python3 -c 'print(__import__("your_module").your_function.__doc__)'
```

## Note

This project builds the core understanding needed before using TensorFlow or PyTorch. Manual implementation helps clarify the role and mechanics of CNN components.
