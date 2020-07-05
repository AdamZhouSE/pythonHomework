piles=eval(input())
h=int(input())
max_k=max(piles)
min_k=int(sum(piles)/h)
re=max_k
for k in range(min_k,max_k+1):
    time=0
    bananas=[i for i in piles]
    while len(bananas)>0:
        for i in range(0,len(bananas)):
            bananas[i]=bananas[i]-k
            time+=1
            if bananas[i]<0:
                bananas[i]=0
        while 0 in bananas:
            bananas.remove(0)
    if time<=h:
        re=k
        break
print(re)