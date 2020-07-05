def bestTimeToBuyAndSell(prices):
    ret=[]
    i=0
    while i<len(prices):
        time=[]
        j=i+1
        while j<len(prices) and prices[j]>prices[j-1]:
            j+=1
        if j-1!=i:
            time.append(i)
            time.append(j-1)
            ret.append(time)
        i=j
    return ret

def printFormat(times):
    if len(times)==0: print("没有利润")
    else:
        for i in range(len(times)):
            if i==0: print("({} {})".format(times[i][0],times[i][1]),end="")
            else: print(" ({} {})".format(times[i][0],times[i][1]),end='')
        print()

t=int(input())
while t:
    n=int(input())
    prices=[int(x) for x in input().split()]
    printFormat(bestTimeToBuyAndSell(prices))
    t-=1