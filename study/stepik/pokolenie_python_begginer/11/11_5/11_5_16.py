inp_num_list = input().split()
counter = 0
for i in range(len(inp_num_list)):
    for j in range(i + 1, len(inp_num_list)):
        if inp_num_list[j] == inp_num_list[i]:
            counter += 1
print(counter)
