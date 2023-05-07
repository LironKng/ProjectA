import numpy as np


def local_align_numpy(seq1, seq2, match_score=2, mismatch_score=-1, gap_penalty=-1):
    m, n = len(seq1), len(seq2)

    # Initialize the score matrix and the first row and column to zero
    score_matrix = np.zeros((m + 1, n + 1), dtype=np.int32)
    score_matrix[0, :] = 0
    score_matrix[:, 0] = 0

    max_score = 0
    max_pos = (0, 0)

    # Loop over the rows of the score matrix
    for i in range(1, m + 1):
        # Loop over the columns of the score matrix
        for j in range(1, n + 1):
            match = score_matrix[i - 1, j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = score_matrix[i - 1, j] + gap_penalty
            insert = score_matrix[i, j - 1] + gap_penalty

            # Set the current cell to the maximum of the three possible values and zero
            score_matrix[i, j] = max(match, delete, insert, 0)

            # Update the maximum score and position
            if score_matrix[i, j] > max_score:
                max_score = score_matrix[i, j]
                max_pos = (i, j)

    return score_matrix, max_score, max_pos


def traceback_numpy(score_matrix, seq1, seq2, max_pos, match_score=2, mismatch_score=-1, gap_penalty=-1):
    i, j = max_pos
    align1, align2 = [], []

    for _ in range(score_matrix.size):
        current_score = score_matrix[i, j]
        diagonal_score = score_matrix[i - 1, j - 1]
        up_score = score_matrix[i - 1, j]
        left_score = score_matrix[i, j - 1]

        if current_score == 0:
            break

        if current_score == diagonal_score + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif current_score == up_score + gap_penalty:
            align1.append(seq1[i - 1])
            align2.append("-")
            i -= 1
        elif current_score == left_score + gap_penalty:
            align1.append("-")
            align2.append(seq2[j - 1])
            j -= 1

    align1.reverse()
    align2.reverse()

    return "".join(align1), "".join(align2)


if __name__ == "__main__":
    seq1 = "TGTTACGG"
    seq2 = "GGTTGACTA"

    score_matrix, max_score, max_pos = local_align_numpy(seq1, seq2)
    print("Score matrix:\n", score_matrix)
    print("Max score:", max_score)
    print("Max position:", max_pos)

    alignment1, alignment2 = traceback_numpy(score_matrix, seq1, seq2, max_pos)
    print("Alignment 1:", alignment1)
    print("Alignment 2:", alignment2)
