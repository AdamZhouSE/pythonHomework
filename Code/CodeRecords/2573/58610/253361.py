from math import pow

def get_num(num: int) -> int:
    if num % 2 == 0:
        return int(pow(2, pow(3, (num - 2) / 2)))
    else:
        return int(pow(2, pow(2, (num - 1) / 2)))

for _ in range(eval(input())):
    print(get_num(eval(input())))