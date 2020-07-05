n=int(input())
list1=input().split(' ')
num=[]
for i in range(len(list1)):
    num.append(int(list1[i]))
count=0
for  i in range(len(num)):
    for j in range(i+1,len(num)):
        for k in range(j+1,len(num)):
            if num[i]<num[j] and num[j]<num[k]:
                count=count+1
print(count,end='')