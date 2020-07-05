num=int(input())
for k in range(num):
    l=input().split(" ")
    n1=int(l[0])
    n2=int(l[1])
    people=[]
    for i in range(n1):
        people.append(i+1)
    sum=0
    flag=0
    result=[]
    while(sum<n1):
        for i in range(n1):
            if people[i]!=0:
                flag=flag+1
            if people[i]>0 and flag>0 and flag%n2==0:
                sum=sum+1
                people[i]=0
                result.append(i+1)
    #print(result)
    print(result[len(result)-1])
