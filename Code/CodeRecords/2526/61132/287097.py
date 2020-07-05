def fil(l):
    return list(filter(lambda x:str(x).isdigit(),l))

l1=input()[1:-1].split(',')
l2=input()[1:-1].split(',')
print(sorted(fil(l1)+fil(l2)))