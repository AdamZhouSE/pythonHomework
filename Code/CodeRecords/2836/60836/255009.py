"""
有一天，史派克感兴趣于如何以非降序对整数 a1，a2，...，an 进行排序
他唯一可以执行的操作是 shift
也就是说，她可以将序列的最后一个元素移到其开头：
a1，a2，...，an → an，a1，a2，...，an-1。
帮助史派克计算：对序列进行非降序排序所需的最少操作数是多少？
"""

def equal(arr,sorted_arr):
    for i in range(len(arr)):
        if arr[i]!=sorted_arr[i]:
            return False
    return True


n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

sorted_arr=sorted(arr)
num_of_operation=0
for i in range(len(arr)):
    if equal(arr, sorted_arr):
        break
    arr.insert(0,arr[len(arr)-1])
    del arr[len(arr)-1]
    num_of_operation=num_of_operation+1

if num_of_operation==len(arr):
    print("-1")
else:
    print(num_of_operation)