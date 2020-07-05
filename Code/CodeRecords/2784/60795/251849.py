arr=input().split(' ')
num=int(arr[0])
city=int(arr[1])
re=[]
for i in range(0,city):
    array=[int(n) for n in input().split(' ')]
    max,mark=-1,-1
    for j in range(0,num):
        if array[j]>max:
            max=array[j]
            mark=j
    re.append(mark)
r,count=-1,0
for i in range(0,len(re)):
    a=re[i]
    m=1
    for j in range(i+1,len(re)):
        if re[j]==a:
           m=m+1
    if m>count:
        count=m
        r=a
res=r+1
print(res)

