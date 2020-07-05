def change(nums):
    for i in range(len(nums)):
        if nums[i]==1:
            k=1
            for j in range(i+1,len(nums)):
                if nums[j]==1:
                    k+=1
                else:
                    break
            nums[i]=k
    return nums
n=""
l=[]
while(n!="]"):
    n=input()
    l.append(n)
l=l[1:-1]
matrix=[]
for i in l:
    k=[]
    for j in i:
        if j.isdigit():
            #print(j)
            k.append(int(j))
    matrix.append(k)
#print(matrix)
for i in range(len(matrix)):
    matrix[i]=change(matrix[i])
#print(l)
#print(matrix)
all_max=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            continue
        a=matrix[i][j]
        min_=a
        max_=a
        for k in range(i+1,len(matrix)):
            if matrix[k][j]==0:
                break
            min_=min(matrix[k][j],min_)
            max_=max((k-i+1)*min_,max_)
        all_max=max(max_,all_max)
print(all_max)

