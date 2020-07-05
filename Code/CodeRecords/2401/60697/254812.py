k=int(input())
res=0
i=0
tmp=0
while tmp<k:
    tmp+=2**i
    i+=1
ans=[]
while k>=1 :
    ans.append(k)
    k=((2**i)-1-((2**(i-1))-1)+(2**i)-1-k)//2
    i-=1
ans.reverse()
print(ans)
