n=int(input())
ai=input().split(" ")
bi=input().split(" ")
ai=list(int(a) for a in ai)
bi=list(int(b) for b in bi)
tot=sum(ai)
bi=sorted(bi)
two=bi[-1]+bi[-2]
if(tot<=two):
    print("YES")
else:
    print("NO")