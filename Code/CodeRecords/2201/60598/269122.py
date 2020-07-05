times = int(input())
def check(num):
    j = 2
    while j*j < num:
        if num % j == 0:
            return False
        j += 1
    return j*j != num


for i in range(times):
    pencil = input().split(" ")
    total = int(pencil[0]) + int(pencil[1])
    third = 1
    while 1:
        if check(total+third):
            print(third)
            break
        third += 1
