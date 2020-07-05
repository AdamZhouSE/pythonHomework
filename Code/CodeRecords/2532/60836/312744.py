"""
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8
arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序
之后再连接起来，使得连接的结果和按升序排序后的原数组相同
我们最多能将数组分成多少块?
"""

arr=[int(m) for m in eval(str(input()))]

i=1
num=1
begin=0
while(i<len(arr)):
    if(max(arr[begin:i])<=min(arr[i:len(arr)])):
        num+=1
        begin=i
    i+=1

print(num)