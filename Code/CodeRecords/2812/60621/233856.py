n=int(input())
candidate=[int(x) for x in input().split()]
ans=len(set(candidate))-candidate.count(0)
if(ans==0):
    print(1)
else:
    print(ans)