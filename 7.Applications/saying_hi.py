import re

if __name__ == "__main__":
    pat = r'^[Hh][Ii]\s[^Dd].*'

    n = int(input())
    for nr in range(n):
        line = input()
        find = re.search(pat, line)

        if find:
            print(line)