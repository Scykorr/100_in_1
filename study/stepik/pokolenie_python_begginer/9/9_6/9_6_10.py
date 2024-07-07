first_inp_num = int(input())
second_inp_num = int(input())
sum_cubes = first_inp_num ** 3 + second_inp_num ** 3
cube_sum = (first_inp_num + second_inp_num) ** 3
print(
    'Для чисел {num_a} и {num_b}:\n'
    '  Сумма кубов: {num_a}**3 + {num_b}**3 = {sum_cubes}\n'
    '  Куб суммы: ({num_a} + {num_b})**3 = {cube_sum}'.format(
        num_a=first_inp_num,
        num_b=second_inp_num,
        sum_cubes=sum_cubes,
        cube_sum=cube_sum,
    ))
