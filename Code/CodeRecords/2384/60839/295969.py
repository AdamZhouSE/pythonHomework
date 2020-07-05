def func(lis):
    lis1=sorted(lis)
    for i in range(1,lis1[len(lis1)-1]+2):
        if lis1.count(i)==0:
            return i


n=int(input())
ans=[]

for i in range(0,n):
    a=int(input())
    x=input()
    lis=list(map(int,x.split(" ")))
    ans.append(func(lis))
for i in ans:
    print(i)
    