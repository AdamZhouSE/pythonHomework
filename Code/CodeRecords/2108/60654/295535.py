a = int(input())
sum = 0
for i in range(1,a+1):
    while i>0:
        if i%10 == 1:
            sum += 1
        i //= 10
print(sum)        