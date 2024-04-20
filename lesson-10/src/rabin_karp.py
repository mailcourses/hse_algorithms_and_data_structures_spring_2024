#! /usr/bin/env python3

def rapin_karp(text: str, pattern: str) -> bool:
    n = len(text)
    m = len(pattern)

    hT = sum([ord(text[i]) for i in range(m)])
    hP = sum([ord(pattern[i]) for i in range(m)])

    # T = abcde
    # P = cde
    for i in range(0, n - m + 1):
        if hT == hP:
            counter = 0
            for j in range(m):
                if text[i + j] == pattern[j]:
                    counter += 1
            if counter == m:
                return True
        # Recalculate hash if not last iteration
        if i != n - m:
            hT += ord(text[i + m]) - ord(text[i])
    return False

def main():
    print(rapin_karp("abcde", "cde"))
    print(rapin_karp("abcde", "abc"))
    print(rapin_karp("abcde", "bcd"))
    print(rapin_karp("abcde", "wer"))

if __name__ == "__main__":
    main()
