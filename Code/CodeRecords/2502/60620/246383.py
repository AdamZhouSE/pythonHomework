n=int(input())
num=0
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n-1):
    num+=max(a[i],a[i+1])
print(num)
             

             