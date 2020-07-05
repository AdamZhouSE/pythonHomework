"""
给定一个数组，任务是将其分为两组S1和S2，以使它们的和之间的绝对差最小
"""

def ad(l):
    number=0
    for i in l:
        number=number+i
    return number

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=string_list[i]
    arr=[int(k) for k in string_list[i+1].split(" ")]
    arr.sort()

    Min=max(arr)
    ad_of_all=ad(arr)

    for m in range(len(arr)):
        k=m+1
        while k<=len(arr):
            num1=ad(arr[m:k])
            num2=ad_of_all-num1
            if num1>=num2:
                num=num1-num2
            else:
                num=num2-num1
            if Min>num:
                Min=num
            k=k+1

    print(Min)

    i=i+2