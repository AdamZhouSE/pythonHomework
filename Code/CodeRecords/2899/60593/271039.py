x=int(input())
i,ans=0,False
while(True):
    tmp=4**i
    if(tmp==x):
        ans=True
    if(tmp>x):
        break
    i+=1
print('true'if ans else 'false')