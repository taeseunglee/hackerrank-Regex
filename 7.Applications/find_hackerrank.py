import re

if __name__ == "__main__":
    n = int(input())
    for nl in range(n):
        line = input()
        cnt = 0

        isStart = re.search(r'^hackerrank.*', line)
        if isStart:
            cnt += 1

        isEnd = re.search(r'.*hackerrank$', line)
        if isEnd:
            cnt += 2

        if cnt == 3:
            print("0")
        elif cnt == 0:
            print("-1")
        else:
            print(cnt)