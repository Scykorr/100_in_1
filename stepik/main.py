for num in range(1729, 1730):
    counter = 0
    for num_a in range(1, 13):
        for num_b in range(1, 13):
            for num_c in range(1, 13):
                for num_d in range(1, 13):
                    if (num_a ** 3 + num_b ** 3) == (
                            num_c ** 3 + num_d ** 3) == num and num_a != num_b and num_a != num_c and num_a != num_d and num_b != num_c and num_b != num_d and num_c != num_d:
                        print(num)
