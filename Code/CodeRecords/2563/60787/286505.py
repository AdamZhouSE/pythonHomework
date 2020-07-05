def cal(n,k):
    re=[]
    if k==1:
        re.append(n)
    else:
        while n>0:
            re.insert(0,n%k)
            temp=0
            while n>=k:
                temp+=1
                n=n-k
            n=temp
    return re

p=input()
a=p[1:len(p)-1]
n=0
for i in range(len(a)-1,-1,-1):
    n+=pow(10,i)*int(a[i])
k=1
while True:
    temp=cal(n,k)
    for i in range(0,len(temp)):
        if temp[i]!=1:
            break
    else:
        break
    k+=1
print(k)