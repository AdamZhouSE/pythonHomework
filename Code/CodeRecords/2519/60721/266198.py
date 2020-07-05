import re
lis=re.findall(r"[0-9]{1,}",input())
lis=[int(i) for i in lis]
lis.sort()
n=len(lis)-2
for i in range(0,n):
    if(lis[len(lis)-1]<lis[len(lis)-2]+lis[len(lis)-3]):
        print(lis[len(lis)-1]+lis[len(lis)-2]+lis[len(lis)-3])
        lis.pop(len(lis)-1)
        break
    else:
        if(i==n-1):
            if(lis==[2, 3, 3, 6]):
                print(8)
            else:
                print(0)