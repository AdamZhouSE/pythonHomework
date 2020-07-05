from functools import reduce

total=int(input())
pis=list(map(int,input().split()))
all=reduce(lambda x,y:x+y,pis)
print('%.6f'% (all/(total*100)*100))