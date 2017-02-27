import re

if __name__ == "__main__":
    pat = r'[A-Z]{5}[A-Z0-9]{5}'

    n = int(input())
    for nl in range(n):
        line = input()

        isMatched = re.match(pat, line)

        if isMatched:
            print("YES")
        else:
            print("NO")