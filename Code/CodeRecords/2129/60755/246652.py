num = int(input())
sum = 0
while num != 1:
    num = num/2 
    if num - int(num) != 0:
        sum = sum + 1
        num = int(num)
    sum = sum + 1
print(sum)