inp_str = input()
count_f = inp_str.count('f')
if count_f == 1:
    print(-1)
elif count_f == 0:
    print(-2)
else:
    first_index = inp_str.find('f')
    print(inp_str[first_index + 1:].find('f') + first_index + 1)
