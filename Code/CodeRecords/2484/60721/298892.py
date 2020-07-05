T=int(input())
for i in range(0,T):
    s=input()
    s1=list(map(int , input().split(" ")))
    s2=list(map(int , input().split(" ")))
    lis=[]
    for i in s1:
        if(i not in lis):
            lis.append(i)
    for i in s2:
        if(i not in lis):
            lis.append(i)
    print(len(lis))       