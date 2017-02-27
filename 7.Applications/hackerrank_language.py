import re

if __name__ == "__main__":
    pat = r'^\d{5} (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'

    n = int(input())
    for nr in range(n):
        line = input()
        find = re.search(pat, line)
        if find:
            print("VALID")
        else:
            print("INVALID")