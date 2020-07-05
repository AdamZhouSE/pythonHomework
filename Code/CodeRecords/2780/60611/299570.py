num=int(input())
for i in range(num):
    t=input()
    t=sorted(list(map(int,input().split(" "))))
    k=int(input())
    s=1
    for j in t:
        s*=j
    print(s%k)