n=int(input())
for i in range(n):
    n,m=input().split()
    l1 = list(input().split())
    l2 = list(input().split())
    num=len(set(l1)&set(l2))
    print(num)