num=int(input())
for i in range(num):
    t=int(input())
    l=sorted(list(map(int,input().split(" "))))
    if t%2==0:
        print((l[len(l)//2-1]+l[len(l)//2])//2)
    else:
        print(l[len(l)//2])