l=eval(input())
lower=int(input())
upper=int(input())
Sum=0
for i in range(1,len(l)+1):
    for j in range(0,len(l)-i+1):
        tmp=sum(l[j:j+i])
        if tmp>=lower and tmp<=upper:
            Sum+=1
print(Sum)