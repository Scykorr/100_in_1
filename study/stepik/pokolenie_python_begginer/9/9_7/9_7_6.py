inp_step = int(input())
inp_string = input()
alph = 26
for i in range(len(inp_string)):
    word = ord(inp_string[i]) - inp_step
    if word < 97:
        word += alph
    print(chr(word), end='')
