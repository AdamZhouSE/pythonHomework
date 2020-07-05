def isValid(H:int,K:int,piles:list):
    sum =  0
    for pile in piles:
        temp1  =pile//K
        temp2 = pile/K
        if(temp1<temp2):
            sum = sum+temp1+1
        else:
            sum  = sum+temp1
    return sum<=H


piles = eval(input())
H = int(input())
listRes =[]
for i in range(1,sum(piles)):
    if(isValid(H,i,piles)):
        listRes.append(i);
print(min(listRes))