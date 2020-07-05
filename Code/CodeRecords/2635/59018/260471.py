K=int(input())
last=1
while(last<K):
    last=5*last+1
while(last>1):
    if(last-1==K):
        return 0
    last=(last-1)/5
    K=K%last

return 5