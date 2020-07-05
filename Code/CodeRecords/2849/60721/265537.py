n=int(input())
lis=input().split(" ")
lis=[int(i) for i in lis]
a=min(lis)
for x in lis:
    if(x%a==0):
        continue
    else:
        a=-1
        break
print(a)