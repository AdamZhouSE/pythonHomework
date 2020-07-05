"""
给定整数数组A []，请根据元素的频率对数组进行排序
也就是说，频率较高的元素排在第一位
如果两个元素的频率相同，则以较小的数字为准
"""

def delete(n,arr):
    m=0
    while m<len(arr):
        if arr[m]==n:
            del arr[m]
        else:
            m+=1


n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    arr=[int(m) for m in string_list[i+1].split(" ")]
    arr.sort()

    num_list=[]
    amount_list=[]
    while len(arr)>0:
        num_list.append(arr[0])
        amount_list.append(arr.count(arr[0]))
        delete(arr[0],arr)

    result_list=[]
    while len(amount_list)>0:
        m=0
        while m<max(amount_list):
            result_list.append(str(num_list[amount_list.index(max(amount_list))]))
            m+=1
        del num_list[amount_list.index(max(amount_list))]
        del amount_list[amount_list.index(max(amount_list))]


    print(" ".join(result_list),end='')
    print(" ")

    i=i+2