inp_string = input()
first_el = inp_string.find('h')
second_el = inp_string.rfind('h')
print(inp_string[:first_el] + inp_string[second_el+1:])
