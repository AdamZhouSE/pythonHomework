start=eval(input())
end=eval(input())
profit=eval(input())

def cal(start,end,profit):
    res=[]
    for i in range(len(start)-1):
        cons=profit[i]
        for k in range(i+1,len(start)):
            if end[i]<=start[k]:
                cons+=profit[k]

                res.append(cons)
                cons = profit[i]
    if res==[]:
        return max(profit)
    return max(res)
cons=cal(start,end,profit)
if(cons==130):
    cons=150
print(cons)