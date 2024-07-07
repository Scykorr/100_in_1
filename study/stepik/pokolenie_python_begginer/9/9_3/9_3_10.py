inp_string = input()
lowers_letter = 'qwertyuiopasdfghjklzxcvbnm'
counter = 0
for el in inp_string:
    if el in lowers_letter:
        counter += 1
print(counter)
