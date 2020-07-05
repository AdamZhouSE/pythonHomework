op=input().split()
flowers=[]
price=[]
while not op[0]=="-1":
    if op[0]=="1":
        w,c=int(op[1]),int(op[2])
        if not c in price:
            flowers.append(w)
            price.append(c)
    if op[0]=="2":
        i=price.index(max(price))
        del price[i]
        del flowers[i]
    if op[0]=="3":
        i=flowers.index(min(flowers))
        del price[i]
        del flowers[i]
    op=input().split()
print(sum(flowers),sum(price))