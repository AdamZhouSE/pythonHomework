"""
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]
请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案
"""

arr=[int(m) for m in list(eval(str(input())))]

i=1
while(i<len(arr)):
    if(arr[i]==arr[i-1] and i!=len(arr)-1):
        arr.append(arr[i])
        del arr[i]
    elif(arr[i]==arr[i-1] and i==len(arr)-1):
        arr.insert(0,arr[i])
        del arr[i]
        i+=1
    else:
        i+=1

print(arr)