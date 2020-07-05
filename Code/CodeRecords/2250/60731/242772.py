num=int(input())
list=[]
res=[]
for i in range(num):
    a,b=map(int,input().split(','))
    list.append([a,b])
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def maxNumber(list):
    res=[]
    for i in range(len(list)):
        index=1
        for j in range(len(list)):
            if list[i]==list[j]:
                index+=1
        res.append(index-1)
    return max(res)
for i in range(len(list)):
    list1=[]
    index=1
    for j in range(len(list)):
        if j!=i:
            x1=list[i][0]
            y1=list[i][1]
            x2=list[j][0]
            y2=list[j][1]
            if x1==x2 and y1==y2:
                index+=1
            else:
                x=x2-x1
                y=y2-y1
                gcdnum=gcd(x,y)
                x=x/gcdnum
                y=y/gcdnum
                list1.append([x,y])
    index+=maxNumber(list1)
    res.append(index)
print(max(res))