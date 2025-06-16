# Probability and Statistics Fundamentals

## General

### What is Probability?

Probability is a way to measure how likely an event is to happen. It’s a number between 0 (impossible) and 1 (certain). For example, the probability of flipping heads on a fair coin is 0.5.

### Basic Probability Notation

* $P(A)$: Probability that event A happens
* $P(A^c)$: Probability that event A does **not** happen (complement of A)
* $P(A \cap B)$: Probability that both A and B happen (intersection)
* $P(A \cup B)$: Probability that A or B or both happen (union)

### What is Independence? What is Disjoint?

* **Independent events:** Two events A and B are independent if the occurrence of one does NOT affect the probability of the other.
* **Disjoint (Mutually Exclusive) events:** Events that cannot happen at the same time (e.g., rolling a 2 and a 5 on one dice roll).

### What is a Union? Intersection?

* **Union ($A \cup B$)**: Event that either A or B or both happen.
* **Intersection ($A \cap B$)**: Event that both A and B happen at the same time.

### What are the General Addition and Multiplication Rules?

* **Addition rule:**
  $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
  (Adds probabilities but subtracts overlap to avoid double counting)

* **Multiplication rule:**

  * For independent events: $P(A \cap B) = P(A) \times P(B)$
  * For dependent events: $P(A \cap B) = P(A) \times P(B|A)$ (Probability of B given A)

### What is a Probability Distribution?

A probability distribution tells you all possible outcomes of a random variable and their probabilities.

### What is a Probability Distribution Function? Probability Mass Function?

* **Probability Distribution Function:** Another name for a function that gives probabilities for outcomes.
* **Probability Mass Function (PMF):** Used for discrete random variables; gives the probability that the variable equals a specific value.

### What is a Cumulative Distribution Function?

The CDF gives the probability that a random variable is **less than or equal to** a certain value. It accumulates probabilities up to that point.

### What is a Percentile?

A percentile tells you the value below which a certain percentage of data falls. For example, the 50th percentile (median) splits data in half.

### What is Mean, Standard Deviation, and Variance?

* **Mean:** The average value of a dataset.
* **Variance:** The average squared difference from the mean — measures spread.
* **Standard Deviation:** The square root of variance — how spread out values are around the mean, in the original units.

### Common Probability Distributions

* **Binomial Distribution:** Models number of successes in fixed number of independent yes/no trials.
* **Normal Distribution:** The famous bell curve; continuous and symmetric around the mean.
* **Poisson Distribution:** Models count of events happening in a fixed interval of time or space.
* **Uniform Distribution:** All outcomes are equally likely.
