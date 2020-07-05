a=input()
cons=[]
count=0
for i in range(2,int(a)):
    for k in range(1,i+1):
        if i%k==0:
            count+=1
    if count<3:
        cons.append(i)
    count=0
print(len(cons))