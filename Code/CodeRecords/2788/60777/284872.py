b=int(input())
bs=[int(x) for x in input().split(' ')]
g=int(input())
gs=[int(x) for x in input().split(' ')]
c=0
while(bs!=[]):
    pre=min(bs)
    if((pre-1) in gs):
        gs.remove(pre-1)
        c+=1
    elif(pre in gs):
        gs.remove(pre)
        c+=1
    elif(pre+1 in gs):
        gs.remove(pre+1)
        c+=1
    bs.remove(pre)
    
print(c)
    