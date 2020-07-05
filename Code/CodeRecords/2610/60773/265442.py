num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    sum=0
    for i in range(len(l)):
        res=[]
        for j in range(i,len(l),1):
            if l[j] in res:
                break
            else:
                res.append(l[j])
                #print(res)
                sum=sum+len(res)
    print(sum)