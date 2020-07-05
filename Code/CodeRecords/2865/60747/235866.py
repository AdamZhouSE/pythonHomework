n=int(input())
m=int(input())
num=[0for i in range(n)]
for i in range(n):
    num[i]=int(input())
num.sort()
count=1
s=num[n-1]
a=0
for i in range(n):
    if m>s:
        count = count + 1
        s=s+num[n-2-i]
    else:
        print(count)
        a=-1
        break
if a!=-1:
    print(count)