
def common(arr):
    flag=1
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            flag=0
            break
    return flag

def strictlyIncreasing(arr):
    flag=1
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            flag=0
    return flag

def strictlyDecreasing(arr):
    flag=1
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            flag=0
    return flag

def find_common_index(arr):
    index_arr=[]
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            index_arr.append(i)
    return index_arr



def check(arr):
    flag=False
    maxpointStart=arr.index(max(arr))
    maxpointEnd=len(arr)-maxpointStart-1
    left=arr[:maxpointStart]
    right=arr[maxpointEnd:]
    if strictlyIncreasing(left) and strictlyDecreasing(right):
        flag=True
    return flag

n=int(input())
s=input().split(' ')
arr=[int(i) for i in s]
if check(arr):
    print('YES')
else:
    print("NO")

# 
# arr=[[3,2,1],\
#      [4,5,5,6],\
#      [4,4,2],\
#      [5,7,11,11,2,1],\
#      [5,5,6,6,1],\
#      [1,5,5,5,4,2],\
#      [7],\
#      [1,2,3,2,1],
#      [1,2,1,2],\
#      [3,3,3,3,3,3]]
# for i in arr:
#     print(i,check(i))

