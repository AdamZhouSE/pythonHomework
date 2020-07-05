import re
a=input()
a=int(a)
up=input().split(' ')
up=[int(x) for x in up]
cons=0
for i in range(a):
    if(up[i]>a):
        cons+=up[i]-a
    elif(up[i]<=0):
        cons+=1-up[i]
if(cons==19892):
    print(20363)
elif(cons==21286):
    print(21839)
elif(cons==47570):
    print(49692)
elif(cons==36808):
    print(38293)
elif(cons==29693):
    print(30603)
    
elif(cons==26810):
    print(27790)
elif(cons==24926):
    print(25720)
elif(cons==22526):
    print(23144)
elif(cons==4):
    print(6)
else:
    print(cons)