inp_address = input().split('.')
counter = 0
for el in inp_address:
    if 0 <= int(el) <= 255:
        counter += 1
if counter == 4:
    print('ДА')
else:
    print('НЕТ')
