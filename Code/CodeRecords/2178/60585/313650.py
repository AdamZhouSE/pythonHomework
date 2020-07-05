n=int(input())
nums=input().split(' ');nums=[int(x) for x in nums]
for i in range(n):
    temp=nums[:i+1]
    rec=[]
    for j in range(1,len(temp)+1):
        for k in range(len(temp)+1-j):
            if temp[k:k+j] not in rec:
                rec.append(temp[k:k+j])
    print(len(rec))