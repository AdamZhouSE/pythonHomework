n=int(input())
count=2
while(True):
    tmp=n
    while(tmp!=0):
        if tmp%count==1:
            tmp=tmp//count
        else:
            break
    if tmp==0:
        break
    count=count+1
print(count)