t = int(input())
for i in range(t):
    temp = list(input().split())
    num1 = temp[0]
    num2 = temp[1]
    n1 = 0
    n2 = 0
    length1 = len(num1) - 1
    length2 = len(num2) - 1
    for j in num1:
        n1 = n1 + int(j) * pow(2, length1)
        length1 = length1 - 1
    for j in num2:
        n2 = n2 + int(j) * pow(2, length2)
        length2 = length2 - 1
    print(n1 * n2)
