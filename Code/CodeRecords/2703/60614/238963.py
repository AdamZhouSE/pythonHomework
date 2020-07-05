arr = input()
lines = arr[1:-2].split("], ")
nums=[int(n) for n in (lines[0])[1:].split(",")]
matrix = [0]*len(nums)
matrix[0]=nums
for i in range(1,len(nums)):
    matrix[i]=[int(n) for n in (lines[i])[1:].split(",")]
friends=[]
for i in range(0,len(nums)):
    friends.append(i)
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if(matrix[i][j]==1):
            friends[j]=friends[i]
print(len(list(set(friends))))