n=int(input())
li=[]
for i in range(n):
    arr=input().split()
    li.append(arr)
m=int(input())
for i in range(m):
    s=input()
    re=[]
    for j in range(len(li)):
        if li[j].count(s)>=1:
            re.append(j+1)
    if len(re)==0:
        print(' ')
    else:
        for j in range(len(re)):
            print(re[j],end=' ')
        print()