inp_string = input().upper()
print('Аденин: {adenin_amount}\nГуанин: {guanine_amount}\nЦитозин: {citozine_amount}\nТимин: {timin_amount}'.format(
    adenin_amount=inp_string.count('А'),
    guanine_amount=inp_string.count('Г'),
    citozine_amount=inp_string.count('Ц'),
    timin_amount=inp_string.count('Т'),
))
