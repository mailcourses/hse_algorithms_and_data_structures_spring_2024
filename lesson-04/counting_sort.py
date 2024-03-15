#! /usr/bin/env python3
# Структурка:
#   - имя
#   - фамилия
#   - возраст
#   - адрес


from dataclasses import dataclass
from typing import Sequence
import random


@dataclass(order=True)
class Person:
    balance: int = 0
    age: int = 0


def count_sort(persons: Sequence[Person], key) -> Sequence[Person]:
    max_key = max(key(p) for p in persons)
    min_key = min(key(p) for p in persons)

    counts = [0 for _ in range(min_key, max_key + 1)]
    persons_sorted = [None for _ in persons]

    key_ = lambda x: key(x) - min_key

    for p in persons:
        counts[key_(p)] += 1

    for i, c in enumerate(counts[1:], start=1):
        counts[i] = counts[i-1] + c

    for p in persons[::-1]:
        c_idx = key_(p)
        idx = counts[c_idx] - 1
        counts[c_idx] -= 1
        persons_sorted[idx] = p

    return persons_sorted


def main():
    random.seed(0)

    persons = [Person(balance=random.randint(-100, 100)) for i in range(15)]
    persons_sorted = count_sort(persons, key=lambda p: p.balance)

    print([p.balance for p in persons])
    print([p.balance for p in persons_sorted])



if __name__ == "__main__":
    main()
