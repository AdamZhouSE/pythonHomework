n=int(input())
ji=1
list1=[]
cifang=1
s=0
for i in range(20):
    for j in range(i+1):
        if j ==0:
            ji=1
        else:
            ji=ji*j
    list1.append(ji)  
for i in range(n):
    cifang=10*cifang

for i in list1:
    if i%cifang==0 and i%(cifang*10)!=0:
        s+=1
print(s)        