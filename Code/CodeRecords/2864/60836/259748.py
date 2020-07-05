"""
给你一个数组 a，里面有 n 个整数
你每次可以选择数组中的一个元素 ak，从数组中删掉它
再删掉所有值等于ak + 1 或者 ak  - 1 的元素,这样你可以得到 ak 分
你可以重复进行多次该操作，请问你最后最多能得多少分？
"""

def delete(arr,n):
    m=0
    while m<len(arr):
        if arr[m]==n:
            del arr[m]
        else:
            m=m+1


n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

score=0
while len(arr)>0:
    a=max(arr)
    num_a = arr.count(a)
    if a-1 not in arr:
        score=score+a*num_a
        delete(arr,a)
    else:
        b = a - 1
        num_b = arr.count(b)
        if a-2 in arr:
            c = a - 2
            num_c = arr.count(c)
            if b*num_b>a*num_a+c*num_c:
                score = score + b*num_b
                delete(arr,a)
                delete(arr,b)
                delete(arr,c)
            else:
                score=score+a*num_a
                delete(arr,a)
                delete(arr,b)
        else:
            if b*num_b>a*num_a:
                score+=b*num_b
            else:
                score+=a*num_a
            delete(arr, a)
            delete(arr, b)
print(score)