import random

fruits = [6, 6, 6, 7, 7, 7, 11, 11, 11, 12, 12, 12, 12, 13]
for _ in range(555):
    random_fruit = random.choice(fruits)
    print(random_fruit)