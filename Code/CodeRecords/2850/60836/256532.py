"""
Lahub 很无聊，所以他在纸上玩一个游戏：
在纸上写上 n 个数，只可能是 0 或者 1
他只允许做一次操作：对连续的 k 个数执行 x = 1 - x 的操作
请问在执行这样一个操作后，纸上最多能有多少个 1。
"""

def change(i,k,arr):
    num=0
    for m in range(len(arr)):
        if m<i or m>k:
            if arr[m]==1:
                num=num+1
        else:
            if arr[m]==0:
                num=num+1
    return num


n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

max_num=0
for i in range(len(arr)):
    k=i
    while k<len(arr):
        num=change(i,k,arr)
        if num>max_num:
            max_num=num
        k=k+1

print(max_num)