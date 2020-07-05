str1=input().split(' ')
N=int(str1[0])
M=int(str1[1])
num=[]
num.append(-1)
for i in range(N):
    num.append(0)
for i in range(M):
    list1=input().split(' ')
    if list1[0]=='0':
        for j in range(int(list1[1]),int(list1[2])+1):
            if num[j]==0:
                num[j]=1
            else:
                num[j]=0
    elif list1[0]=='1':
        sum=0
        for j in range(int(list1[1]),int(list1[2])+1):
            if num[j]==1:
                sum=sum+1
        print(sum)