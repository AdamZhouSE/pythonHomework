n=int(input())
l=list(input())
print('%.14f'%(sum(map(lambda x:{'A':4,'B':3,'C':2,'D':1,'E':0,'F':0}[x],l))/n),end='')