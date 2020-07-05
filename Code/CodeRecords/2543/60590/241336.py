t = int(input())
for k in range(t):
    n=int(input())
    nums=input().split(' ')
    nums = [str(x) for x in nums]
    record=[]
    for i in range(1,n+1):
        mins=[]
        for j in range(n-i+1):
            temp=nums[j:j+i]
            mins.append(min(temp))
        record.append(max(mins))
        mins.clear()
    #record = [int(x) for x in record]
    print(' '.join(record))