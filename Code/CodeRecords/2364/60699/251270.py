k=int(input())
ans=0
for i in range(11,k+1):
    dict={}
    while i >0:
        dict[i%10]=dict.get(i%10,0)+1
        if dict[i%10]>1:
            ans+=1
        i//=10
print(ans)