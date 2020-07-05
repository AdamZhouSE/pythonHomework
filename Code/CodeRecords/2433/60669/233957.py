'''
题目描述:
给出一个区间的集合，请合并所有重叠的区间。

输入描述:
一个区间的集合

输出描述:
合并后的区间的集合
'''

input=input()
input= input[1:-1]
list=input.split(",")

#本质上是个冒泡
for i in range(0 , len(list) - 1):
    for j in range(0,len(list)-i-1):
        num1 = ''.join([x for x in list[j] if x.isdigit()])
        num2 = ''.join([x for x in list[j+1] if x.isdigit()])
        if int(num1)>int(num2):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp


result="["
first=True
for item in list:
    if first==True:
        result+=item
        result+=','
        first=False
    else:
        index=list.index(item)
        if ']' in item:
            if index==len(list)-1 :
                result+=item
                result+=','
                first=True
            elif '[' in list[index+1]:
                num1 = ''.join([x for x in list[index] if x.isdigit()])
                num2 = ''.join([x for x in list[index + 1] if x.isdigit()])
                if int(num1)!=int(num2):     # 防止前一个区间尾和后一个区间头是一样的
                    result += item
                    result += ','
                    first = True


result=result[0:-1]+']'
arr=eval(result)
print(arr)