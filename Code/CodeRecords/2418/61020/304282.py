# [total_jumbo, ]

num_of_toma = int(input())
num_of_chee = int(input())

temp = num_of_toma - 2 * num_of_chee
total_jumbo = (temp) // 2
if total_jumbo * 2 != temp:
    print('[]')
else:
    total_small = num_of_chee - total_jumbo
    if total_small >= 0 and total_jumbo >= 0:
        print([total_jumbo, total_small])
    else:
        print('[]')
