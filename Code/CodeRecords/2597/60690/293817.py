str=input().split(" ")
beauty,price=0,0
prices=[]
beautys=[]
while str[0]!="-1":
    if str[0]=="1":
        b=int(str[1])
        p=int(str[2])
        if p not in prices:
            prices.append(p)
            beautys.append(b)
    elif str[0]=="2":
        if len(prices)!=0:
            index=prices.index(max(prices))
            prices.pop(index)
            beautys.pop(index)
    else:
        if len(prices)!=0:
            index=prices.index(min(prices))
            prices.pop(index)
            beautys.pop(index)
    str=input().split(" ")
for e in beautys:beauty+=e
for e in prices:price+=e
print(beauty,end=" ")
print(price,end="")