"""
给定一个由N个元素组成的整数序列，现在有两种操作：
1 add a
在该序列的最后添加一个整数a，组成长度为N + 1的整数序列
2 mid 输出当前序列的中位数
中位数是指将一个序列按照从小到大排序后处在中间位置的数
（若序列长度为偶数，则指处在中间位置的两个数中较小的那个）
"""

N=int(input())
arr=[int(m) for m in str(input()).split(" ")]
n=int(input())
instruction=[]
for i in range(n):
    instruction.append(str(input()).split(" "))

for i in range(n):
    if(instruction[i][0]=="add"):
        arr.append(int(instruction[i][1]))
    else:
        arr.sort()
        if(len(arr)%2==0):
            print(arr[len(arr)//2-1])
        else:
            print(arr[len(arr)//2])