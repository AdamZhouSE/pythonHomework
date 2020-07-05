n=int(input())
l=list(input())
print(sum(map(lambda x:{'A':4,'B':3,'C':2,'D':1,'F':0}[x],l))/n)