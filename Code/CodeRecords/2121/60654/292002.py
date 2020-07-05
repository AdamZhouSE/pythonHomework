def x(num):
    list1 = []
    while num != 0:
        if num%10 not in list1:
            list1.append(num%10)
        else:
            return False
        num //= 10
    return True
sum = 0
xy = int(input())
for i in range(10**xy):
    if x(i+1):
        sum += 1
print(sum)