num = int(input())

res = 0
while num != 1:
    if num % 2 == 0:
        res+=1
        num = num /2
    else:
        res+=1
        num = num -1
print(res)