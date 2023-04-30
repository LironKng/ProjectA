import sys


def make_matrix(sizex, sizey):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0] * (sizey + 1) for i in range(sizex + 1)]


class ScoreParam:
    """The parameters for an alignment scoring function"""

    def __init__(self, gap, match, mismatch):
        self.gap = gap
        self.match = match
        self.mismatch = mismatch


def local_align(x, y, print_matrix, score=ScoreParam(-7, 10, -5)):
    """Do a local alignment between x and y"""
    # create a zero-filled matrix
    A = make_matrix(len(x), len(y))
    high = 0
    opt_loc = (0, 0)
    # fill in A in the right order
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            # the local alignment recurrence rule:
            A[i][j] = max(
                A[i][j - 1] + score.gap,
                A[i - 1][j] + score.gap,
                A[i - 1][j - 1] + (score.match if x[i - 1] == y[j - 1] else score.mismatch),
                0
            )

            # track the cell with the largest score
            if A[i][j] >= high:
                high = A[i][j]
                opt_loc = (i, j)

    # print the matrix A
    if print_matrix:
        for row in A:
            print(row)

    # backtrack to find the indices that led to the best score
    i, j = opt_loc
    route = [(i, j)]
    while A[i][j] > 0:
        if A[i - 1][j - 1] >= A[i - 1][j] and A[i - 1][j - 1] >= A[i][j - 1]:
            i, j = i - 1, j - 1
        elif A[i][j - 1] >= A[i - 1][j] and A[i][j - 1] >= A[i - 1][j - 1]:
            j = j - 1
        else:
            i = i - 1
        route.append((i, j))

    # reverse the indices list to get the order from start to end
    route = route[::-1]

    # return the opt score, the best location, and the indices that led to it
    return high, opt_loc, route


def main():
    if len(sys.argv) < 3:
        print("Usage: python localAlign.py sequence1 sequence2 --print_matrix")
        sys.exit(1)

    x = sys.argv[1]
    y = sys.argv[2]
    print_matrix = True if len(sys.argv) > 3 and sys.argv[3] == "--print_matrix" else False

    # call the function with the given inputs
    best, optloc, indices = local_align(x, y, print_matrix, ScoreParam(-7, 8, -5))
    threshold = 20
    # check if the best score is above the threshold
    if best >= threshold:
        print(f"\nThe route goes through: {indices}\nWhile {optloc} have the highest score of: {best}\n")
    else:
        print("\nThe two sequences are not aligned.\n")


if __name__ == '__main__':
    main()
