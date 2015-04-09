# Matrix_rotation_naive.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import itertools


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print('A[%d,%d] = %d' % (i, j, A[i][j]), end='  ')
        print()


def check_answer(A):
    k = itertools.count(1)
    for j in range(len(A) - 1, -1, -1):
        for i in A:
            assert next(k) == i[j]


# @include
def rotate_matrix(A):
    for i in range(len(A) // 2):
        for j in range(i, len(A) - i - 1):
            temp = A[i][j]
            A[i][j] = A[-1 - j][i]
            A[-1 - j][i] = A[-1 - i][-1 - j]
            A[-1 - i][-1 - j] = A[j][-1 - i]
            A[j][-1 - i] = temp
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = itertools.count(1)
        A = []
        for i in range(1 << n):
            A.append([next(k) for j in range(1 << n)])
        print_matrix(A)
        rotate_matrix(A)
        check_answer(A)
        print()
        print_matrix(A)
    else:
        for _ in range(100):
            n = random.randint(1, 10)
            k = itertools.count(1)
            A = []
            for i in range(1 << n):
                A.append([next(k) for j in range(1 << n)])
            rotate_matrix(A)
            check_answer(A)


if __name__ == '__main__':
    main()