tomato=int(input())
cheese=int(input())
jumbo=tomato-2*cheese
res=[]
if jumbo%2==0:
    jumbo=int(jumbo/2)
    small=cheese-jumbo
    if jumbo>=0 and small>=0:
        res.append(jumbo)
        res.append(small)
print(res)