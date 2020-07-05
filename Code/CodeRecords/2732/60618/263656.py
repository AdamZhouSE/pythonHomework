t=int(input())
for i in range(t):
    a,b,c=map(eval,input().split())
    re=(a**b)%c
    print(re)
    