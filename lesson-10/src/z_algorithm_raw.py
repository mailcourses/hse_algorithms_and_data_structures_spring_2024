#! /usr/bin/env python3

# S = P$T
#.    01234
#            l r 
# P = ababa$dabacababcd...
#     0       i
# z = 00301003010
def z_algorithm(text: str, pattern: str) -> int:
    combined = pattern + "$" + text
    z = [0] * len(combined)
    l, r = 0, 0
    for i in range(1, len(combined)):
        if i > r:
            j = 0
            s1 = pattern[i:]
            s0 = pattern[0:len(pattern)-i+1]
            for j in range(len(s1)):
                if s1[j] == s0[j]:
                    z[i] += 1
                else:
                    break
            #l, r = i, i + z[i] - 1
        #if i <= r:
        #    z[i] = min(r - i + 1, z[i - 1])
        if z[i] == len(pattern):
            return i
    return -1

def main():
    p = "ababa"
    t = "dabacababacd"
    print(p[0:2])
    print(z_algorithm(t, p))
    print(z_algorithm(t, "sdfsdfsdf"))

if __name__ == "__main__":
    main()
