numlist=input().split('+')
length=len(numlist)
for i in range(length- 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(length - i - 1):  # j为列表下标
            if numlist[j] > numlist[j + 1]:
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
result=""
for x in numlist:
    result+=x
    result+="+"
print(result[0:2*length-1])