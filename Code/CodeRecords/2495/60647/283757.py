str=input()
list2=input()
list2=list2.strip('[')
list2=list2.strip(']')
list=''
for i in list2:
    if i!='"':
        list=list+i
list=list.split(',')

def num(str1,str2,res):
    list1=[]
    list2=[]
    for i in str1:
        list1.append(i)
    for i in str2:
        list2.append(i)
    list=[]
    for i in range(len(list1)):
        if list1[i] in list2:
            list.append(list2.index(list1[i]))
        else:
            return res
    for i in range(len(list)-1):
        if int(list[i])>int(list[i+1]):
            return res
    res.append(str1)
    return res
res=[]
for i in range(len(list)):
    num(list[i],str,res)
def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):
            if len(nums[j]) < len(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
res=bubble_sort(res)
if len(res)!=0:
    print(res[0])