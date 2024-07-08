inp_amount = int(input())
curr_num = int(input())
result_list = list()
for _ in range(inp_amount - 1):
    inp_num = int(input())
    result_list.append(inp_num + curr_num)
    curr_num = inp_num
print(result_list)
