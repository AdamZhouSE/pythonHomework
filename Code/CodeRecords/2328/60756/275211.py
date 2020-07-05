from itertools import permutations
arr=list(map(int,input().split(",")))
ans=(-1,-1)
for h1,h2,m1,m2 in permutations(arr):
    hours=10*h1+h2
    mins=10*m1+m2
    if 0<=hours<24 and 0<=mins<60:
        ans=max(ans,(hours,mins),key=lambda x:60*x[0]+x[1])
print("{:0>2d}:{:0>2d}".format(ans[0],ans[1])if ans[0]!=-1 else "")