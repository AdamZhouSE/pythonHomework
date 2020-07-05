Nums=int(input())
ai=input().split(" ")
bi=input().split(" ")
ai=list(int(a) for a in ai)
bi=list(int(b) for b in bi)
total=sum(ai)
bi=sorted(bi)
two=bi[-1]+bi[-2]
if(total<=two):
    print("YES")
else:
    print("NO")