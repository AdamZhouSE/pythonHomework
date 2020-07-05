n=int(input())
num=[0for i in range(n)]
a=0
for i in range(n):
    num[i]=input()
str="".join(num)
p=[]
for i in str:
    p.append(i)
b=set(p)
if len(b)!=2:
    print("NO")
else:
    for i in range(n):
        if num[i]==num[n-1-i]:
            continue
        else:
            print("NO")
            a=-1
            break
    if a!=-1:
        print("YES")