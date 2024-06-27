first_inp_x_cel = int(input())
first_inp_y_cel = int(input())
second_inp_x_cel = int(input())
second_inp_y_cel = int(input())
if abs(first_inp_x_cel - second_inp_x_cel) == abs(
        first_inp_y_cel - second_inp_y_cel) or first_inp_x_cel == second_inp_x_cel or first_inp_y_cel == second_inp_y_cel:
    print('YES')
else:
    print('NO')
