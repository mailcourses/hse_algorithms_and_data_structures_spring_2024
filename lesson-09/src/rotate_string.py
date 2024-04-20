#! /usr/bin/env python3

# text =   abadea
# goal = deaaba
# S = goal+goal = deaabadeaaba
def rotate_string(text: str, goal: str) -> bool:
    if len(text) != len(goal):
        return False

    n = len(text)

    for i in range(n):
        k = 0
        if text[0] == goal[i]:
            k = i
        else:
            continue
        for j in range(k, n+k):
            if goal[j%n] != text[j-k]:
                break
        return True
    return False

def main():
    print(rotate_string("abadea", "deaaba"))
    print(rotate_string("qwerty", "deaaba"))

if __name__ == "__main__":
    main()

