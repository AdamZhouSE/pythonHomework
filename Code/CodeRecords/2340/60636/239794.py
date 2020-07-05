number=int(input())
lists=[]
for i in range(number):
    source=[]
    num=int(input())
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(len(lists)):
    a=0
    count=0
    while(a<len(lists[i])-1):
        if(lists[i][a+1]<lists[i][a]):
            x=a
            while(lists[i][a+1]<lists[i][x]):
                a=a+1
            if(((a==len(lists[i])-1)&(lists[i][a]>=lists[i][x]))|(a!=len(lists[i])-1)):
                sum=0
                for y in range(x+1,a):
                    sum=sum+lists[i][y]
                count=count+(a-x-1)*lists[i][x]-sum
            else:
                a=x
                t=lists[i].value(max(lists[i][a+1:]))
                if(t==a+1):
                    break
                else:
                    sum=0
                    for y in range(x+1,t):
                        sum=sum+lists[i][y]
                    count=count+(t-x-1)*lists[i][t]-sum
                a=t
        else:
            a=a+1
print(count)