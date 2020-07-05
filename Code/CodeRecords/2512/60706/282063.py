str1=input().split(' ')
N=int(str1[0])
P=int(str1[1])
num=[]
num.append(0)
list1=input().split(' ')
for i in range(len(list1)):
    num.append(int(list1[i]))
M=int(input())
for i in range(M):
    str1=input().split(' ')
    if str1[0]=='1':
        for j in range(int(str1[1]),int(str1[2])+1):
            num[j]=num[j]*int(str1[3])
    elif str1[0]=='2':
        for j in range(int(str1[1]),int(str1[2])+1):
            num[j]=num[j]+int(str1[3])
    else:
        sum=0
        for j in range(int(str1[1]),int(str1[2])+1):
            sum=sum+num[j]
        print(sum%P)