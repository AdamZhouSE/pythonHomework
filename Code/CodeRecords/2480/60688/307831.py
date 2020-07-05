T=int(input())
for a in range(0,T):
    N=int(input())
    num=input().split(" ")
    num=list(int(b) for b in num)
    num=sorted(num,key=lambda x: x%2)
    for c in range (0,len(num)):
        print(num[c],end=" ")
    print()