num=list(input().split(" "))
n=int(num[2])
up=int(num[1])
l=int(num[0])
number=[]
for i in range(l):
    number.append(1)
for i in range(n):
    res=[]
    tem=list(input().split(" "))
    if int(tem[1])>int(tem[2]):
        a=tem[1]
        tem[1]=tem[2]
        tem[2]=a
    if tem[0]=="C":
        for j in range(int(tem[1])-1,int(tem[2])):
            number[j]=int(tem[3])
    if tem[0]=="P":
        for j in range(int(tem[1])-1,int(tem[2])):
            if number[j] not in res:
                res.append(number[j])
        print(len(res))