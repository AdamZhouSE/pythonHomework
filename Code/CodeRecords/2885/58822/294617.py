num=int(input())
sum=0
for i in range(num):
    k=int(input())
    n=input().split(' ')
    n=list(map(int,n))
    he=0
    li=[]
    sum=0
    for j in range(len(n)):
        if(n[j]%3==0):
            he+=1
        else:
            sum=sum+n[j]
    he=he+int(sum/3)
    print(he)