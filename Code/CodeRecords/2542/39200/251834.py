string=input();
A=string[1:-1:1].split(',')
D=[]
it=iter(A)
for x in it:
    D.append(int(x))

D.sort()
i=0
temp=0
count=1
maxcount=0
while(i<len(D)):
    if(i!=0):
        if(D[i]==temp+1):
            count+=1
        else:
            if(count>maxcount):
                maxcount=count
            count=1
    temp=D[i]
    i+=1
print(maxcount)