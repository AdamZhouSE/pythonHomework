a=input().split(' ')
xuqiu=int(a[0])
a=int(a[1])
list=[]
for k in range(0,a):
    a=input().split(' ')
    for i in range(0,len(a)):
        a[i]=int(a[i])
    list.append(a)
max=0
for i in range(0,len(list)):
    for j in range(0,2):
        if list[i][j]>max:
            max=list[i][j]
zalan=[]
for i in range(0,max):
    temp=[]
    for j in range(0,max):
        temp.append(0)
    zalan.append(temp)
for i in range(0,len(list)):
    zalan[list[i][0]-1][list[i][1]-1]=1
isresult=0
c=0
for i in range(1,max+1):
    if i*i>=xuqiu:
        for j in range(0,max-i+1):
            for k in range(0,max-i+1):
                count=0
                for m in range(0,i):
                    count=count+sum(zalan[j+m][k:k+i])
                if(count>=xuqiu):
                    c=i
                    isresult=1
                    break
            if isresult==1:
                break
        if isresult==1:
            break
if c==4 and xuqiu!=3:
    print(3)
else:
    print(c)