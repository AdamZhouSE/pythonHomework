T=int(input())
for m in range(T):
    k=int(input())
    N=int(input())
    nums=input().split(" ")
    for i in range(N):
        nums[i]=int(nums[i])
    parts=[]
    part=[]
    for i in range(N-1):
        part.append(nums[i])
        if nums[i+1]<nums[i]:
            parts.append(part)
            part=[]
    part.append(nums[-1])
    parts.append(part)
    new_parts=[]
    for i in range(len(parts)):
        if len(parts[i])!=1:
            new_parts.append(parts[i])
    parts=new_parts
    result=0
    for i in range(len(parts)):
        result=result+parts[i][-1]-parts[i][0]
    if k<len(parts):
        d=len(parts)-k
        m=[]
        for i in range(len(parts)-1):
            m.append(parts[i][-1]-parts[i+1][0])
        m.sort()
        for i in range(d):
            result-=m[i]
    print(result)
