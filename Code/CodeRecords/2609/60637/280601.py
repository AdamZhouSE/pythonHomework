tests=(int)(input())
for i in range(tests):
    demand=input().split(' ')
    nums=input().split(' ')
    num=[]
    frequency=[]
    unique_num=[]
    for j in nums:
        if(j not in num):
            num.append(j)
            frequency.append(1)
        else:
            frequency[num.index(j)]+=1
    for j in range(len(num)):
        if(frequency[j]==1):
            unique_num.append(num[j])
    if((int)(demand[1])>len(unique_num)):
        print(-1)
    else:
        print(unique_num[(int)(demand[1])-1])