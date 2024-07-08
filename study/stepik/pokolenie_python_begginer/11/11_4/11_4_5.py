string_amount = int(input())
result_list = list()
for _ in range(string_amount):
    inp_str = input()
    if inp_str not in result_list:
        result_list.append(inp_str)
print(*result_list, sep='\n')
