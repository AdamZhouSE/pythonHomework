t=int(input())
for i in range(t):
    list1=input().split(' ')
    N=int(list1[0])
    K=int(list1[1])
    list2=input().split(' ')
    max=0
    for i in range(len(list2)-K+1):
        sum=0
        for j in range(i,i+K):
            sum=sum+int(list2[j])
        if sum>max:
            max=sum
    print(max)