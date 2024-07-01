from math import log

inp_num = int(input())
total = 0
for num in range(1, inp_num + 1):
    total += (1 / num)
print(total - log(inp_num))