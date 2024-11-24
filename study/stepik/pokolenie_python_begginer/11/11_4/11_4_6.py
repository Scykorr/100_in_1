string_amount = int(input())
result_list = list()
for _ in range(string_amount):
    result_list.append(input())
test_string = input()
for i in result_list:
    if test_string.lower() in i.lower():
        print(i)
