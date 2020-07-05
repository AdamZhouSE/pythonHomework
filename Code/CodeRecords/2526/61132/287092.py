def fil(l):
    return list(filter(lambda x:str(x).isdigit(),l))

l1=eval(input())
l2=eval(input())
print(sorted(fil(l1)+fil(l2)))