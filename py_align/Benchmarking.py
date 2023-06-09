import timeit
import matplotlib.pyplot as plt
import subprocess

from nonParallelSw import *
from numpySw import *
from parallelSw import *
from numbaSw import *


def generate_random_sequence(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def run_comparison(seq1, seq2):
    print(f"Sequence lengths: {len(seq1)}, {len(seq2)}")

    start_time = timeit.default_timer()
    score_matrix_parallel, max_score_parallel, max_pos_parallel = local_align(seq1, seq2)
    end_time = timeit.default_timer()
    non_parallel_time = end_time - start_time
    print(f"Non Parallel implementation time: {end_time - start_time:.5f} seconds")

    start_time = timeit.default_timer()
    score_matrix_parallel, max_score_parallel, max_pos_parallel = smith_waterman_parallel(seq1, seq2, num_threads=20)
    end_time = timeit.default_timer()
    parallel_time = end_time - start_time
    print(f"Parallel implementation time: {end_time - start_time:.5f} seconds")

    start_time = timeit.default_timer()
    score_matrix_vectorized, max_score_vectorized, max_pos_vectorized = local_align_numpy(seq1, seq2)
    end_time = timeit.default_timer()
    vectorized_time = end_time - start_time
    print(f"Vectorized implementation time: {end_time - start_time:.5f} seconds")

    start_time = timeit.default_timer()
    score_matrix_vectorized, max_score_vectorized, max_pos_vectorized = smith_waterman_numba(seq1, seq2)
    end_time = timeit.default_timer()
    numba_time = end_time - start_time
    print(f"Numba implementation time: {end_time - start_time:.5f} seconds")

    start_time = timeit.default_timer()
    subprocess.run(['./c_align/c_align.exe', seq1, seq2, "-q"])
    end_time = timeit.default_timer()
    c_time = end_time - start_time
    print(f"C implementation time: {end_time - start_time:.5f} seconds")

    print()
    return non_parallel_time, parallel_time, vectorized_time, numba_time, c_time


def plot_performance(sizes, n, p, v, numba, c):
    fig, ax = plt.subplots()

    ax.scatter(sizes, n, linewidth=2, label="Non Parallel Performance")
    ax.scatter(sizes, v, linewidth=2, label="Vectorized Performance")
    ax.scatter(sizes, p, linewidth=2, label="Parallel Performance")
    ax.scatter(sizes, numba, linewidth=2, label="Numba Performance")
    ax.scatter(sizes, c, linewidth=2, label="C Performance")

    # customize the plot
    ax.set_title('Different implementations of Smith Waterman')
    ax.set_xlabel('sequence size')
    ax.set_ylabel('performance [s]')
    ax.legend(loc='best')

    # display the plot
    plt.savefig("perf-comparison.png")


if __name__ == "__main__":
    seq_sizes = np.arange(100, 4000, 100)
    nonParallel_perf = []
    parallel_perf = []
    vectorized_perf = []
    vectorizedEff_perf = []
    numba_perf = []
    c_perf = []
    for seq_size in seq_sizes:

        seq1 = generate_random_sequence(seq_size)
        seq2 = generate_random_sequence(seq_size)
        nonParallel_perf_elem, parallel_perf_elem, vectorized_perf_elem, numba_perf_elem, \
            c_perf_elem = run_comparison(seq1, seq2)

        nonParallel_perf.append(nonParallel_perf_elem)
        parallel_perf.append(parallel_perf_elem)
        vectorized_perf.append(vectorized_perf_elem)
        numba_perf.append(numba_perf_elem)
        c_perf.append(c_perf_elem)

    plot_performance(seq_sizes, nonParallel_perf, parallel_perf, vectorized_perf, numba_perf, c_perf)
