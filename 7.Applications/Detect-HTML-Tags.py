import re

if __name__ == "__main__":
    regex_pattern = r'<\s*(\w+)'
    num_lines = int(input())

    tag_list=[]
    for i in range(num_lines):
        line = input()
        splited_line = re.split('(<\s*(\w+))', line)

        for sub_line in splited_line:
            match = re.search(regex_pattern, sub_line)
            if match:
                tag_list.append(str(match.group(1)))

    tag_list = sorted(set(tag_list))
    print(";".join(tag_list))