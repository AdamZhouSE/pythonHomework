num=int(input())
s=input()
l=s.split(",")
min=100
for i in range(len(l)):
    l[i]=int(l[i])
for i in range(len(l)-1):
    sum=0
    for k in range(len(l)-i):
        sum=sum+l[i+k]
        if sum>=num:
            if k+1<min:
                min=k+1
            break
if max(l)>=num: print(1)
else:
    if min==100: print(0)
    else: print(min)
#print(s)
#print(num)
