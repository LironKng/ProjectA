# Smith Waterman Algorithm for Local Alignment
This project implements the Smith Waterman algorithm, a dynamic programming algorithm used for local sequence alignment. 
The algorithm compares two sequences and identifies the best local alignment between them, meaning the best matching subsequence, even if it is a small part of the larger sequence.

# Implementation
The project contains several implementations of the Smith Waterman algorithm in different programming languages. 
These implementations can be found in the following files:

* localAlignDraft.c: C draft implementation of non-parallel matrix operations
* localAlignDraft.py: Python draft implementation of non-parallel matrix operations
* localAlignNonParallel.py: Python implementation of non-parallel matrix operations
* localAlignNumPy.py: Python implementation using NumPy for matrix operations
* localAlignNumba.py: Python implementation using Numba, a just-in-time (JIT) compiler for Python
