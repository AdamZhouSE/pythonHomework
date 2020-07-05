n=int(input())
sum=0
while n != 1 and n != 4:
    while n != 0:
        sum += (n % 10) ** 2
        n = n // 10
    n = sum
    sum = 0
if n == 1:
    print(True)
else:
    print(False)