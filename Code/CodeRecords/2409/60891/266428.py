inp = input()
chips = [int(i) for i in inp.split(',')]
count_odd = 0
count_even = 0
for i in chips:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(min(count_odd, count_even))