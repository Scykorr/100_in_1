inp_str = input()
letters = 'АВЕКМНОРСТУХ'
if (inp_str[0] in letters) and (inp_str[1:4].isdigit()) and (inp_str[4] in letters) and (inp_str[5] in letters) and (
        inp_str[6] == '_') and (inp_str[7:].isdigit()) and (9 <= len(inp_str) <= 10):
    print('YES')
else:
    print('NO')
