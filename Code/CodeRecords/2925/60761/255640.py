n=int(input())
carin=list(map(int,input().split(" ")))
ci=carin[:]
carout=list(map(int,input().split(" ")))
co=carout[:]
result=0
while(len(carout)>0):
    if(carin[0]==carout[0]):
        carin.pop(0)
        carout.pop(0)
    else:
        carin.remove(carout.pop(0))
        result+=1
print(result)