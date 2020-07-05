n=int(input(""))
light=list(map(int,input("").split(" ")))

off=0
for i in range(2,n-2):
    if light[i-1]==0 and light[i]==1 and light[i+1]==0:
        if light[i-2]==1 and light[i+2]==1:
            light[i]==0
            off+=1
for i in range(1,n-1):
    if light[i-1]==1 and light[i]==0 and light[i+1]==1:
        light[i+1]=0
        off+=1
print(off)