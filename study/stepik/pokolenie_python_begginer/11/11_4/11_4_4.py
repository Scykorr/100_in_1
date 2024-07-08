num_amount = int(input())
result_list = list()
for _ in range(num_amount):
    result_list.append(int(input()))
del result_list[result_list.index(max(result_list))]
del result_list[result_list.index(min(result_list))]
print(*result_list, sep='\n')
