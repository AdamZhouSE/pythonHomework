"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长
如果不能形成任何面积不为零的三角形，返回 0
"""

arr=[int(m) for m in eval(str(input()))]

perimeter=0
if(len(arr)<3):
    perimeter=0
else:
    arr.sort()
    i=len(arr)-3
    while(i>=0):
        a=arr[i]
        b=arr[i+1]
        c=arr[i+2]
        if(a+b>c):
            perimeter=a+b+c
            break
        else:
            i-=1

print(perimeter)