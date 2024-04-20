#! /usr/bin/env python3

def calculateZ(pattern: str):
    z = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = 0
        s1 = pattern[i:]
        s0 = pattern[0:len(pattern)-i+1]
        for j in range(len(s1)):
            if s1[j] == s0[j]:
                z[i] += 1
            else:
                break
    return z

def KnuthMorrisPratt(text: str, pattern: str) -> bool:
    sp_ = [0] * len(pattern)
    z = calculateZ(pattern)
    n = len(pattern)
    m = len(text)
    #print(z)
    for j in range(n-1, 0, -1):
        i = j + z[j] - 1
        sp_[i] = z[j]
    sp = sp_
    #print(sp_)
    for i in range(n-2, 1, -1):
        sp[i] = max(sp_[i], sp[i+1]-1)
    print(sp)
    c = 0
    p = 0
    while c + (n-p) < m:
        while p < n and text[c] == pattern[p]:
            c += 1
            p += 1
        if p == n:
            return True
        if p == 0:
            c += 1
        #print(f"{c=}, {p=}, {sp[p-1]}, {n=}, {m=}")
        p = sp[p-1]
    return False

def main():
    text = "ababkbababcababdcty"
    #          012345678
    pattern = "ababd"
    print(KnuthMorrisPratt(text, pattern))
    print(KnuthMorrisPratt(text, "34345345345"))

if __name__ == "__main__":
    main()
