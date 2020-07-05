num=[];

for i in range(2,100):
    
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
a=int(input())
for i in range(a):
    n=int(input())
    res=pow(num[n-1],2)+1
    print(res)