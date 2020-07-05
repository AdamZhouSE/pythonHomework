n=input().split(' ')
num=int(n[0])
limit=int(n[1])
k=input().split(' ')
ma=num-1
time=0
while(int(k[0])<=limit):
    if(int(k[0])<=limit):
        time+=1
        ma=ma-1
        del k[0]
    if(len(k)==0):
        break
if(len(k)!=0):
    while(int(k[ma])<=limit):
        time+=1
        ma=ma-1
        del k[(ma+1)]
        if(len(k)==0):
            break
print(time)