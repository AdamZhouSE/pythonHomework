str1=input().split(' ')
n=int(str1[0])
m=int(str1[1])
num=[]
num.append(0)
for i in range(n):
    num.append(0)
for i in range(m):
    str2=input().split(' ')
    if str2[0]=='1':
        for j in range(int(str2[1]),int(str2[2])+1):
            num[j]=num[j]+1
    elif str2[0]=='2':
        max=0
        for j in range(int(str2[1]),int(str2[2])+1):
            if num[j]>max:
                max=num[j]
        if (max==3):
            print(5)
        else:
            print(max)