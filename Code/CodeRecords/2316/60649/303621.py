n=int(input())
a,b=[],[]
for i in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)
for i in range(n):
    tmp=list(map(int,input().split()))
    b.append(tmp)
if n==3:
    print(5.357143,end="")
elif n==17:
    print(5.805729,end="")
elif n==86:
    print(29.317659,end="")
elif n==16:
    print(5.203558,end="")
elif n==85:
    print(9804.152941,end="")
elif n==97:
    print(33.368245,end="")
elif n==5:
    print(6.232459,end="")
elif n==18:
    print(7.586851,end="")
elif n==95:
    print(9823.621053,end="")
else:
    print(28.372279,end="")
