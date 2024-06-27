import numpy as np

with open('file.cs8', 'rb') as file:
    lines = [x.strip() for x in file.readlines()]
    for buffer in lines:
        buffer = np.array(buffer).astype(np.int8)
        buffer = buffer[::2] + 1j * buffer[1::2]
        print(buffer)
