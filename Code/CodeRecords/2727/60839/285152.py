def func(s1,s2)->int:
    lis1=sorted(s1)
    lis2=sorted(s2)
    lis=[]
    for i in range(0,len(lis1)):
        if int(lis1[i])>int(lis2[i]):
            lis.append(int(lis1[i])-int(lis2[i]))
        else:
            lis.append(int(lis2[i]) - int(lis1[i]))
    ans=sorted(lis,reverse=True)
    return ans[0]

n=int(input())
ans=[]

for i in range(0,n):
    input()
    s1=input().split(" ")
    s1new=map(eval,s1)
    s2=input().split(" ")
    s2new=map(eval,s2)
    ans.append(func(s1new,s2new))