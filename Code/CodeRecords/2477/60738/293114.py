n=int(input())
for i in range(n):
    t1=list(map(int,input().split()))
    t2=list(map(int,input().split()))
    if min(t1[1],t2[1])>max(t1[3],t2[3]) and min(t1[2],t2[2])>max(t1[0],t2[0]):
        print(1)
    else:
        print(0)
    