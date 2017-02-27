import re

if __name__ == "__main__":
    pat = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'

    n = int(input())
    for nl in range(n):
        line = input()
        isMatch = re.match(pat, line)

        if isMatch:
            print("VALID")
        else:
            print("INVALID")