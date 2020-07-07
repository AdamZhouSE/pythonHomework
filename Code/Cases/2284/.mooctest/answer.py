# Python3 program to find the maximum 
# j – i such that arr[j] > arr[i] 

# For a given array arr[], returns 
# the maximum j – i such that 
# arr[j] > arr[i] 
def maxIndexDiff(arr, n): 
	maxDiff = -1
	for i in range(0, n): 
		j = n - 1
		while(j > i): 
			if arr[j] > arr[i] and maxDiff < (j - i): 
				maxDiff = j - i; 
			j -= 1
	
	return maxDiff 

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxDiff = maxIndexDiff(arr, n) 
    print(maxDiff)