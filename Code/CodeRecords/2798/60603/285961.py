num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
count=0
for i in range(num-2):
    for j in range(i+1,num-1):
        all1=0
        all2=0
        all3=0
        first=i
        second=j
        for m in range(i+1):
            all1+=list[m]
        for m in range(i+1,j+1):
            all2+=list[m]
        for m in range(j+1,num):
            all3+=list[m]
        if((all1==all2)&(all2==all3)):
            count+=1
print(count)