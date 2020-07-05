k=int(input())
for z in range(k):
    n=int(input())
    s=list(map(int,input().split(' ')))
    s.sort()
    print(s[int(input())-1])