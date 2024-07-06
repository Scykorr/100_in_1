inp_string = input()
ciphers = '1234567890'
counter = 0
for el in inp_string:
    if el in ciphers:
        counter += 1
print(counter)
