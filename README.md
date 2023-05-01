# Smith Waterman Algorithm for Local Alignment
This project implements the Smith Waterman algorithm, a dynamic programming algorithm used for local sequence alignment. 
The algorithm compares two sequences and identifies the best local alignment between them, meaning the best matching subsequence, even if it is a small part of the larger sequence.

# Implementation
The project contains several implementations of the Smith Waterman algorithm in different programming languages. 
These implementations can be found in the following files:

* draftSw.c: C draft implementation of non-parallel matrix operations
* draftSw.py: Python draft implementation of non-parallel matrix operations
* nonParallelSw.py: Python implementation of non-parallel matrix operations
* parallelSw.py:  Python implementation of parallel matrix operations
* numpySw.py: Python implementation using NumPy for matrix operations
* numbaSw.py: Python implementation using Numba, a just-in-time (JIT) compiler for Python

In the Benchmarking.py we compare the runtime performance of Smith Watermann algorithm implemented with highly efficient methods.

![image](https://user-images.githubusercontent.com/129160734/235427493-1a37e535-d9b0-4d10-863c-fc14b072c8ed.png)
