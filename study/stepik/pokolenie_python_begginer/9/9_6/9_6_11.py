inp_day = int(input())
inp_weight = float(input())
weight_step = (100 - 88) / 60
true_weight = 100 - inp_day * weight_step
if inp_weight <= true_weight:
    print('Все идет по плану')
else:
    print('Что-то пошло не так')
print('#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {curr_weight} кг, ЦЕЛЬ по ВЕСУ = {true_weight} кг'.format(
    day=inp_day,
    curr_weight=inp_weight,
    true_weight=true_weight,
))
