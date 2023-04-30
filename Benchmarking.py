import random
import string
import timeit
import matplotlib.pyplot as plt
import numpy as np

from localAlignNonParallel import *


def generate_random_sequence(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def run_comparison(seq1, seq2):
    print(f"Sequence lengths: {len(seq1)}, {len(seq2)}")

    start_time = timeit.default_timer()
    score_matrix_parallel, max_score_parallel, max_pos_parallel = local_align(seq1, seq2)
    end_time = timeit.default_timer()
    non_parallel_time = end_time - start_time
    print(f"Parallel implementation time: {end_time - start_time:.5f} seconds")

    print()
    return non_parallel_time


def plot_performance(seq_sizes, n_perf):
    fig, ax = plt.subplots()

    ax.scatter(seq_sizes, n_perf, linewidth=2, label="Vectorized Performance")

    # customize the plot
    ax.set_title('Vectorized implementation vs. Parallel implementation of Smith Watermann')
    ax.set_xlabel('sequence size')
    ax.set_ylabel('performance [s]')
    ax.legend(loc='best')

    # display the plot
    plt.savefig("perf-comparison.png")


if __name__ == "__main__":
    seq_sizes = np.arange(100, 4000, 100)
    n_perf = []
    for seq_size in seq_sizes:

        seq1 = generate_random_sequence(seq_size)
        seq2 = generate_random_sequence(seq_size)
        n_perf_elem = run_comparison(seq1, seq2)
        n_perf.append(n_perf_elem)

    plot_performance(seq_sizes, n_perf)
