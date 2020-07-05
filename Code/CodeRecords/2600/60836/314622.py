"""
给你一个由n个非负整数组成的数列 a_1，a_2，...，a_n。
你将要一个一个摧毁这个数列中的数。并且，现在给你一个由 1 到 n 组成的序列来告诉你每个数被摧毁的时间顺序
每当一个元素被摧毁时，你需要找到这个当前数列中的未被摧毁的数组成的和最大的连续子序列
另外，如果当前剩余的序列是空的的话，最大和就是0
"""

def get(arr):
    length=0
    maxsum=0
    i=0
    while(i<len(arr)):
        if(arr[i]!=0):
            length+=arr[i]
            if(length>maxsum):
                maxsum=length
        else:
            length=0
        i+=1
    return maxsum


n=int(input())

arr=[int(m) for m in str(input()).split(" ")]
destory=[int(m) for m in str(input()).split(" ")]

for i in range(n):
    arr[destory[i]-1]=0
    print(get(arr))