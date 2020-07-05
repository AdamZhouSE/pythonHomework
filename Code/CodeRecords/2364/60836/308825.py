"""
给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数
"""

N=int(input())

i=1
num=0
while(i<=N):
    match = False
    a=list(str(i))
    for m in range(len(a)):
        if(a.count(a[m])>1):
            match=True
    if(match):
        num+=1
    i+=1

print(num)