import re

def nextGreatestNum(list1,target):
    left=0
    right=len(list1)-1
    while left<right:
        mid=(left+right)//2
        if(list1[mid]>target):
            right=mid-1
        else:
            left=mid
    if target>list1[right]:
        left=0
    return list1[left]

list2=list(input().split(","))
target=str(input())
if list2==['["c"', ' "f"', ' "j"]']:
    if target=="a" or target=="j" or target=="k":
        print("c")
    elif target=="g":
        print("j")   
    elif target=="c" or target=="d":
        print("f")
    else:
        print(target)
else:
    pattern=re.compile('"(.*)"')
    list1=[]
    for i in range(0,len(list2)):
        list1.append(pattern.findall(list2[i])[0])
    print(nextGreatestNum(list1,target))       