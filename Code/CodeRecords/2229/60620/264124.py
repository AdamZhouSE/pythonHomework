a=list(map(int,input().split(',')))
x1=0
x2=0
for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[i]>a[j]):
            x1+=1
for i in range(len(a)-1):
    if(a[i]>a[i+1]):
        x2+=1
if(x1==x2):
    print(True)
else:
    print(False)