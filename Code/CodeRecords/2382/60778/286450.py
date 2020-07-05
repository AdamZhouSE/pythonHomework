nums=int(input())
lower_bound=[]
upper_bound=[]
for i in range(nums):
    section=list(map(int,input().split()))
    NF=True
    for i in range(len(lower_bound)):
        if(lower_bound[i]<=section[0] and upper_bound[i]>=section[1]):
            NF=False
            break
    if(NF):
        lower_bound.append(section[0])
        upper_bound.append(section[1])
        for i in range(len(lower_bound)):
            for j in range(len(lower_bound)):
                if(i>=len(lower_bound) or j>=len(lower_bound)):
                    break;
                if(i!=j and lower_bound[i]<=lower_bound[j] and upper_bound[i]>=lower_bound[j]):
                    upper_bound[i]=upper_bound[j]
                    del lower_bound[j]
                    del upper_bound[j]
for i in range(len(lower_bound)):
            for j in range(len(lower_bound)):
                if(i>=len(lower_bound) or j>=len(lower_bound)):
                    break;
                if(i!=j and lower_bound[i]<=lower_bound[j] and upper_bound[i]>=lower_bound[j]):
                    upper_bound[i]=upper_bound[j]
                    del lower_bound[j]
                    del upper_bound[j]
lower_bound.sort()
upper_bound.sort()
for i in range(len(lower_bound)):
    print(lower_bound[i],upper_bound[i])