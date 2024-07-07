inp_string = input()
max_val = 0
max_el = ''
for el in inp_string:
    if inp_string.count(el) >= max_val:
        max_val = inp_string.count(el)
        max_el = el
print(max_el)