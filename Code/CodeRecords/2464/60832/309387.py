n = int(input())
ar = list(map(int, input().split(',')))

Sum=0
ans=len(ar)
templ=0
for i in range(len(ar)):
    Sum+=ar[i]
    while Sum>=n:
        if ans>templ:
            ans=templ

        Sum-=ar[i-templ]
        templ-=1
    templ+=1

print(ans+1)


