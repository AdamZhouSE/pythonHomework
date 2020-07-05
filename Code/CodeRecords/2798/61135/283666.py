n=int(input())
arr=input().split(" ")
arr=list(int(a) for a in arr)
total=sum(arr)
if(total%3!=0):
    print(0)
elif(total==0):
    count=0
    mid=arr[0]
    if(mid==0): count=count+1
    for k in range(1,n):
        mid=mid+arr[k]
        if(mid==0): count=count+1
    res=(count-1)*(count-2)//2
    print(res)
else:
    every=total//3
    mid1=0
    state1=0
    id1=0
    for a in range(0,n):
        mid1=mid1+arr[a]
        if(mid1==every):
            state1=1
            id1=a
            break
    if(state1==0):
        print(0)
    else:
        mid2=0
        count1=0
        id2=id1
        for b in range(id1+1,n):
            mid2=mid2+arr[b]
            if(mid2==0):
                id2=b
                count1=count1+1
        mid3=0
        state2=0
        id3=id2
        for c in range(id2+1,n):
            mid3=mid3+arr[c]
            if(mid3==every):
                state2=1
                id3=c
                break
        if(state2==0):
            print(0)
        else:
            mid4=0
            count2=0
            for d in range(id3+1,n):
                mid4=mid4+arr[d]
                if(mid4==0):
                    count2=count2+1
            if(count1==1): count1=count1+1
            res=(count1+1)*(count2+1)
            print(res)
        