import re

if __name__ == '__main__':
    lines = []
    num_lines = int(input())
    for nl in range(num_lines):
        lines.append(input())
        
    queries = []
    num_queries = int(input())
    for nq in range(num_queries):
        queries.append(input())
    
    for q in queries:
        prog = re.compile("\\b(" + q + "|" + q.replace("our", "or") + ")\\b")

        cnt = 0
        for l in lines:
            cnt += len(prog.findall(l))
        print(cnt)