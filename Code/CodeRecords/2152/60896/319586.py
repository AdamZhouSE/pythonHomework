a=eval(input())
temp=input().split(' ')
temp=map(eval,temp)
list1=list(temp)
temp=input().split(' ')
temp=map(eval,temp)
list2=list(temp)

for i in range(a):
    path=[]
    count=0
    a1=i+1
    while(True):
        if(a1 in path):break
        count+=list1[a1-1]
        path.append(a1)
        a1=list2[a1-1]
    print(count)