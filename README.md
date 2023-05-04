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


# Why the implementation using Numba is significantly faster?
Numba is a Python library that allows developers to write high-performance numerical code in Python without sacrificing readability or ease of development. It works by using a just-in-time (JIT) compiler to translate Python code into machine code at runtime. This means that Numba optimizes the code on the fly, as the code is being executed, rather than ahead of time.
The key idea behind Numba is that it can generate optimized machine code that is specifically tailored to the input data types and shapes that the code is operating on. This is because Python is a dynamically-typed language, which means that the data types of variables are not known until runtime. By analyzing the data types of variables at runtime, Numba can generate machine code that is optimized for those data types.
For numerical computations, Numba can be particularly effective because it can generate machine code that takes advantage of hardware-specific features such as SIMD instructions (which allow for parallel execution of the same instruction on multiple pieces of data) and multiple processor cores. This can lead to significant speedups over standard Python code, which typically runs on a single core and does not take advantage of SIMD instructions.
In summary, Numba is a Python library that allows developers to write high-performance numerical code in Python by using a JIT compiler to translate the code into optimized machine code at runtime. By generating code that is specifically tailored to the input data types and shapes, Numba can achieve significant speedups over standard Python code, particularly for numerical computations.
