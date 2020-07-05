def alex():
    inp=int(input())
    prices=[]
    qualities=[]
    for i in range(inp):
        comp=input().split(" ")
        prices.append(int(comp[0]))
        qualities.append(int(comp[1]))
    for i in range(inp-1):
        if(prices[i]<prices[i+1] and qualities[i]>qualities[i+1]):
            return("Happy Alex")
            break
    return ("Poor Alex")

print(alex())
