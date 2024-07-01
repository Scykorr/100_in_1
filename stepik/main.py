inp_amount_num = int(input())
previous_num = 0
current_num = 1
for _ in range(1, inp_amount_num + 1):
    print(current_num, end=' ')
    previous_num, current_num = current_num, previous_num + current_num
