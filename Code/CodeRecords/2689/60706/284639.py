t=int(input())
for i in range(t):
    str1=input().split()
    list1=list(str1[0])
    list2=list(str1[1])
    sum1=[]
    for i in range(len(list1)):
        sum1.append(list1[i])
    for j in range(len(list2)):
        sum1.append(list2[j])
    for i in range(len(sum1)):
        for j in range(i+1,len(sum1)):
            if sum1[i]==sum1[j]:
                sum1[j]=0
    count=0
    for i in range(len(sum1)):
        if sum1[i]!=0:
            count=count+1
    print(count)