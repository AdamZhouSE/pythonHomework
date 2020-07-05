length=int(input())
for i in range(length):
    num=int(input())
    votes=input().split()
    count=[]
    for j in votes:
        judge=True
        for k in count:
            if k[0]==j:
                k[1]+=1
                judge=False
                break
        if judge:
            count.append([j,1])
    temp=sorted(count,key=lambda x:(-x[1],x[0]))[0]
    print(temp[0]+" "+str(temp[1]))