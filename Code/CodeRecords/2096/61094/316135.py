n = int(input())
l = 0
for i in range(0,n):
    if(i*i==n):
        l = i
        break
    if(i*i>n):
        l = i-1
        break
print(l)