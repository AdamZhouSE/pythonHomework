def jie(i):
    if i==1:
        return 10
    elif i == 2:
        return 9*9
    else:
        return (11-i)*jie(i-1)
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += jie(i)
print(sum) 
    