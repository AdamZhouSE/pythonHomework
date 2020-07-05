num1 = list(input())
num2 = list(input())
n1 = 0
n2 = 0
for i in range(len(num1)):
    n1 += int(num1[i]) * (10 ** (len(num1) - 1 - i))
for j in range(len(num2)):
    n2 += int(num2[j]) * (10 ** (len(num2) - 1 - j))
print(str(n1 * n2))