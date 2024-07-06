inp_message_amount = int(input())
counter = 0
for _ in range(inp_message_amount):
    inp_string = input()
    if inp_string.count('11') >= 3:
        counter += 1
print(counter)
