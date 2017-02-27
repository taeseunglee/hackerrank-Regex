import re

if __name__ == "__main__":
    num_lines = int(input())

    cnt = 0
    for nl in range(num_lines):
        line = input()
        if re.search(r'hackerrank', line, re.I):
            cnt += 1

    print(cnt)