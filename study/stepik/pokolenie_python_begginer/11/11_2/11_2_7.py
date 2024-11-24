rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for index, el in enumerate(rainbow):
    if el == 'Green':
        rainbow[index] = 'Зеленый'
    elif el == 'Violet':
        rainbow[index] = 'Фиолетовый'
print(rainbow)
