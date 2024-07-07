inp_string = input()
if len(inp_string) % 2 == 0:
    step = 0
else:
    step = 1
first_part = inp_string[:len(inp_string) // 2 + step]
second_part = inp_string[len(inp_string) // 2 + step:]
print(second_part + first_part)
