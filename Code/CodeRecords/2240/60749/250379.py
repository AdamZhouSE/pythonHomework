from itertools import combinations
num_array=list(map(int,input().split(",")))

def foraverage(nums):
    sum=0
    for h in nums:
        sum+=h
    return sum/len(nums)
def judge(num_array):
    sum = 0.0
    for x in num_array:
        sum += x
    average = sum / len(num_array)
    
    for i in range(1,len(num_array)):
    
        for t in combinations(num_array,i):
            if average==foraverage(t):
                return True
    return False
print(judge(num_array))