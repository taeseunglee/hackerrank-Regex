import re

regex_ip4 = r'^(\d{1,3}\.){3}\d{1,3}$'
regex_ip6 = r'^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$'

num_lines = int(input())

for nl in range(num_lines):
    line = input()
    re.search(regex_ip4, line)
    
    if re.search(regex_ip4, line):
        # checkt the number limitation
        number_list = re.split('\.', line)
        
        # check the number 0~255
        ip4_flag = True
        for n in number_list:
            int_n = int(n)
            if not ((0 <= int_n) and (int_n <= 255)):
                ip4_flag = False
        
        if ip4_flag:
            print("IPv4")
        else:
            print("Neither")
    elif re.search(regex_ip6, line):
        print("IPv6")
    else:
        print("Neither")