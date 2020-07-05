N=int(input())
l=list(map(int,input().split()))
M=int(input())
for i in range(M):
    s=input().split()
    if s[0]=="add":
        l.append(int(s[1]))
    else:
        l.sort()
        print(l[(len(l)-1)//2])
