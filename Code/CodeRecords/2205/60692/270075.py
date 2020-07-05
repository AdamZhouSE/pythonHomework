from math import factorial
num = int(input())
list1 = []
for i in range(num):
    n = int(input()) // 2
    list1.append(factorial(2 * n)//(factorial(n + 1)*factorial(n)))
for num in list1:
    print(num)