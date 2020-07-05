n = eval(input())
a = [0]*1000
b = [1]*1000
line = input().split(' ')
for i in range(n):
    a[i] = int(line[i])
j = 0
for i in range(1,n):
    if a[i]==a[i-1]:
        b[j]+=1
    else:
        j+=1
sum = 0
for i in range(1,j+1):
    sum = max(sum,min(b[i],b[i-1]))
print(2*sum)