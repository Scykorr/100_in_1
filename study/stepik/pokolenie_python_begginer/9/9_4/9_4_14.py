inp_string = input()
el_amount = inp_string.count('f')
if el_amount == 1:
    print(inp_string.find('f'))
elif el_amount >= 2:
    print(inp_string.find('f'), inp_string.rfind('f'))
else:
    print('NO')
