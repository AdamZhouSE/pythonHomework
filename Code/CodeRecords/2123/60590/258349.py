num = int(input())

def isSqr(num):
    displacement = 3
    while num > 1:
        num -= displacement
        displacement += 2
    return num == 1

print(isSqr(num))