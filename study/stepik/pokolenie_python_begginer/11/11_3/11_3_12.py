inp_amount = int(input())
result_list = list()
for _ in range(inp_amount):
    result_list.append(int(input()))
print(result_list[::2])
