n=int(input())
lis=list(map(int,input().split(" ")))
o=1000000000-1
re=0
for x in lis:
    if(x%2==0):
        re+=x
    else:
        if(x<o):
            o=x
        re+=x
if(re%2==0):
    print(re)
else:
    print(re-o)