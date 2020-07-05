restaurant=list(eval(input()))
vf=input()=='1'
price=int(input())
dist=int(input())
dele=0
size=len(restaurant)
for r in restaurant:
    if r[3]>price or r[4]>dist or (vf and r[2]==0):
        r[1]=0
        dele+=1
restaurant.reverse()
restaurant.sort(key=lambda x:x[1],reverse=True)
restaurant=restaurant[0:size-dele]
rt=[]
for r in restaurant:
    rt.append(r[0])
print(rt)