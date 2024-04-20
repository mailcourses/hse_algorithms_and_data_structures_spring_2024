#! /usr/bin/env python3

def naive_search(text: str, pattern: str) -> int:
	n = len(text)
	m = len(pattern)

	for i in range(0, n-m+1):
	    for j in range(0, m):
	        if text[i + j] != pattern[j]:
	            break
	        if j == m-1:
	            return i
	return -1

def main():
    # 012345
    # abcdef , n = 6
    # def.   , m = 3
    # i = 3, j = 0,1,2  text[3+2]

    print(naive_search("abcdeabc", "bc"))
    print(naive_search("abcdeabc", "yyy"))

if __name__ == "__main__":
    main()
