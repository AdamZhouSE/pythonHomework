n=int(input())
time=[]
waiter,plus=1,0
while(n>0):
    n -= 1
    newtime=input().split()
    time.append(newtime)
time.sort()
for i in range(0,len(time)-1):
    if time[i]==time[i+1]:
        plus += 1
    elif plus>=waiter:
        waiter=waiter+plus
        plus=0
    else:
        plus=0
if plus>=waiter:
    waiter += plus
print(waiter)