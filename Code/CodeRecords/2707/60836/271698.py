"""
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手
计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位  
人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号
第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)
这些情侣的初始座位 row[i] 是由最初始坐在第 i 个座位上的人决定的
"""

arr=eval(input())

i=0
num=0
while i<len(arr)-1:
    if arr[i]!=arr[i+1]+1 and arr[i]!=arr[i+1]-1:
        a=arr[i+1]
        num+=1
        if arr[i]%2==0:
            arr[i+1]==arr[i]+1
            arr[arr.index(arr[i]+1)]=a
        else:
            arr[i+1]==arr[i]-1
            arr[arr.index(arr[i]-1)]=a
    i+=2

print(num)