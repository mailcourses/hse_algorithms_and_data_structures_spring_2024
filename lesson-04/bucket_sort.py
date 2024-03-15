#! /usr/bin/env python3

import numpy
import random

COUNT = 1000

def bucket_sort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(COUNT * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
        #print(f"i={i}, len={len(bucket[i])}")
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


def main():
    #lst = [numpy.random.uniform(0,1) for _ in range(COUNT)]
    lst = [random.random() for _ in range(COUNT)]
    sorted_lst = bucket_sort(lst)
    print(sorted_lst)

if __name__ == "__main__":
    main()
