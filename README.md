# Smith Waterman Algorithm for Local Alignment
This project implements the Smith Waterman algorithm, a dynamic programming algorithm used for local sequence alignment. 
The algorithm compares two sequences and identifies the best local alignment between them, meaning the best matching subsequence, even if it is a small part of the larger sequence.

# Implementation
The project contains several implementations of the Smith Waterman algorithm in different programming languages. 
These implementations can be found in the following files:

* draftSW.c: C draft implementation of non-parallel matrix operations
* draftSW.py: Python draft implementation of non-parallel matrix operations
* nonParallelSW.py: Python implementation of non-parallel matrix operations
* parallelSW.py:  Python implementation of parallel matrix operations
* numpySW.py: Python implementation using NumPy for matrix operations
* numbaSW.py: Python implementation using Numba, a just-in-time (JIT) compiler for Python

In the Benchmarking.py we compare the runtime performance of Smith Watermann algorithm implemented with highly efficient methods.
