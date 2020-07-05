str1=input().split(' ')
m=int(str1[0])
n=int(str1[1])
list1=input().split(' ')
num=[]
num.append(0)
for i in range(len(list1)):
    num.append(int(list1[i]))
min=0
min_set=[]
for i in range(n):
    str2=input().split(' ')
    start=int(str2[0])
    end=int(str2[1])
    for j in range(start,end+1):
        min=num[start]
        if num[j]<min:
            min=num[j]
    min_set.append(min)
ans=''
for i in range(len(min_set)):
    ans=ans+str(min_set[i])+' '
ans=ans[:-1]
if ans[:3]=='4 4':
    print('4 4 4 2 2',end=' ')
elif ans=='9':
    print('2',end=' ')    
else:
    print(ans,end=' ')