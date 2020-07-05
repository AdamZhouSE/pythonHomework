n=int(input())
l=list(input())
res=sum(map(lambda x:{'A':4,'B':3,'C':2,'D':1,'E':0,'F':0}[x],l))/n
print('%.14f'%res if res!=0 else 0,end='')