first_letter_index = 96
result_list = list()
for i in range(1, 27):
    inp_el = chr(first_letter_index + i) * i
    result_list.append(inp_el)
print(result_list)
