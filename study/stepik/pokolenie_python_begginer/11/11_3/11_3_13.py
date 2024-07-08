string_amount = int(input())
result_list = list()
for _ in range(string_amount):
    result_list.append(input())
sign_number = int(input())
for el in result_list:
    if len(el) >= sign_number:
        print(el[sign_number-1], end='')
