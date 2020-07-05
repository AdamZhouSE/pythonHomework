n=int(input())
lis=list(map(int,input().split(" ")))
lis.sort()
m=int(input())
for o in range(0,m):
    s=input()
    if(len(s)>3):
        s=s.split(" ")
        a=int(s[1])
        lis.append(a)
        lis.sort()
    else:
        if(len(lis)%2==0):
            b=(lis[int(len(lis)/2-1)])
        else:b=(lis[int(len(lis)/2)])
        print(b)
        