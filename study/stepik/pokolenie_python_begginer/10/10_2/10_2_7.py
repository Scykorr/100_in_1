inp_str = input()
result_str = ''
for index, el in enumerate(inp_str):
    if index % 3 != 0:
        result_str += el
print(result_str)
