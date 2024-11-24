num_amount = int(input())
num_list = list()
for _ in range(num_amount):
    num_list.append(int(input()))
for num in num_list:
    if num < 0:
        print(num)
for num in num_list:
    if num == 0:
        print(num)
for num in num_list:
    if num > 0:
        print(num)
