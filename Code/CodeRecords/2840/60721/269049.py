n,k=map(int,input().split(' '))
lis=input().split(' ')
str=[list()]*n
for i in range(0,n):
    str[i]=list(lis[i])    
count=0
for i in range(0,n):
    if(str[i].count("4")+str[i].count("7")<=k):
        count+=1
print(count)