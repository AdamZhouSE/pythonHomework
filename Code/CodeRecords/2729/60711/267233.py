import re
sea=re.compile(r'\d+')

num=sea.findall(input())
for i in range(len(num)):
    judge=0
    for j in range(i+1,len(num)):
        if num[j]==num[i]:
            judge=1
            del num[j]
            break
    if judge==0:
        print(num[i])
        break


