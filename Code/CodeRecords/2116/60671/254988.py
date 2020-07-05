
n=int(input())
str0=input()
listt=str0.split(',')
prime=[]
for x in listt:
    prime.append(int(x))
    
list0=[1]
idx=[0]*(len(prime))
plen=len(prime)
while(n>1):
    minnum=min([list0[idx[i]]*prime[i] for i in range(plen)])
    for i in range(plen):
        if(minnum==list0[idx[i]]*prime[i]):
            idx[i]+=1
    n-=1
    list0.append(minnum)
print(list0[-1])