#!/usr/bin/python3
# coding=utf-8


def insertion_sort(A, n):
    for i in range(1,n):
        key = A[i]
        while i > 0 and A[i] < A[i-1] :
            A[i], A [i-1] = A[i-1], A[i]
            i -= 1
    return A


if __name__ == "__main__":
    tests = [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([9, 7, 3, 5, 2, 6], [2, 3, 5, 6, 7, 9]),
        ([-1, 1, -1, 2], [-1, -1, 1, 2]),
    ]

    for test, solution in tests:
        answer = insertion_sort(test, len(test))
        if answer != solution:
            print(
                "`insertion_sort` feilet for listen {:}. ".format(test)
                + "Svaret skulle vært {:}, men var {:}.".format(
                    solution, answer
                )
            )