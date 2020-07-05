from itertools import combinations
num_array=list(map(int,input().split(",")))
sum=0.0
for x in num_array:
    sum+=x
average=sum/len(num_array)
def foraverage(nums):
    sum=0
    for h in nums:
        sum+=h
    return sum/len(nums)
    
for i in range(1,len(num_array)):
    
    for t in combinations(num_array,i):
        if average==foraverage(t):
            print(True)
print(False)