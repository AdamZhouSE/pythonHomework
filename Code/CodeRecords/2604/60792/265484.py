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
pattern=re.compile('"(.*)"')
list1=[]
for i in range(0,len(list2)):
    list1.append(pattern.findall(list2[i])[0])
target=str(input())
print(nextGreatestNum(list1,target))       