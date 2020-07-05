num1 = input()
num2 = input()

para1 = 0
para2 = 0
answer = 0
answer1 = 0
CF = 0
for i1 in range(len(num1) - 1, -1, -1):
    n1 = int(num1[i1])
    for i2 in range(len(num2) - 1, -1, -1):
        n2 = int(num2[i2])
        temp = (n1 * n2) + CF
        CF = 0
        if temp >= 10:
            if i2 != 0:
                while temp >= 10:
                    temp -= 10
                    CF += 1
        else:
            CF = 0

        temp *= pow(10, para2)
        answer1 += temp
        para2 += 1
    answer += answer1 * pow(10, para1)
    para1 += 1
    para2 = 0
    CF = 0
    answer1 = 0

print(answer)