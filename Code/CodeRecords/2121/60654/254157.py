def x(num):
    list1 = []
    while num != 0:
        if num%10 not in list1:
            list1.append(num%10)
        num //= 10
    return list1.__len__()
sum = 0
xy = int(input())
for i in range(10**xy):
    if 1+i== x(i+1):
        sum += 1
print(sum)