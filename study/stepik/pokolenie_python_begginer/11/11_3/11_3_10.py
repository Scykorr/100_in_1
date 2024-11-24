inp_num = int(input())
result_list = list()
for el in range(1, inp_num + 1):
    if inp_num % el == 0:
        result_list.append(el)
print(result_list)
