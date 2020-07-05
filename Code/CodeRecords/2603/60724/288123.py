line=input()
line=line[1:len(line)-1]
nums=line.split(",")
k=int(input())
distance=[]
for i in range(len(nums)):
    nums[i]=int(nums[i])
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        distance.append(abs(nums[i]-nums[j]))
distance.sort()
print(distance[k-1])