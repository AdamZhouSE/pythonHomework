y,m,d=map(int,input().split("-"))
days=0
mday=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(0,m-1):
    days+=mday[i]
days+=d
if m>2 and y!=1900 and y%4==0:
    days+=1
print(days)
    
    