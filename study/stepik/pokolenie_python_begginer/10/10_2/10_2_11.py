inp_str = input()
first_h = inp_str.find('h')
last_h = inp_str.rfind('h')
new_middle_string = inp_str[inp_str.find('h') + 1: inp_str.rfind('h')]
print(inp_str[:first_h + 1] + new_middle_string[::-1] + inp_str[last_h:])
