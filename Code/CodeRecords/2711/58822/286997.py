def dif(a,b):
    num=0
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            num+=1
    return num
n=input()
b=list(eval(n))
times=0
for i in range(len(b)):
    for k in range((i+1),len(b)):
        if(dif(b[i],b[k])==2):
            times+=1
print(times)