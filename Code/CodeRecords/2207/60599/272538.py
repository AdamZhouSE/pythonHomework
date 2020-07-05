k = int(input())
for u in range(k):
    s=list(map(int,input().split(' ')))
    if(s[1]*(s[1]+1)//2<=s[0]):
        print(1)
    else:print(0)

