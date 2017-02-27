import re

if __name__ == "__main__":
    pat = r'^([0-9]{1,3})[ -]([0-9]{1,3})[ -]([0-9]{4,10})$'

    n = int(input())
    for nl in range(n):
        line = input()

        match = re.match(pat, line)
        print("CountryCode=" + match.group(1), end="")
        print(",LocalAreaCode=" + match.group(2), end="")
        print(",Number=" + match.group(3))