first_side = int(input())
second_side = int(input())
third_side = int(input())
if first_side == second_side == third_side:
    print('Равносторонний')
elif (first_side == second_side) or (first_side == third_side) or (second_side == third_side):
    print('Равнобедренный')
else:
    print('Разносторонний')
