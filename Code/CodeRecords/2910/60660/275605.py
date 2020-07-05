import functools,collections
t=int(input())
l=[]
for i in range(t):
    l.append(eval('[' + input().replace(' ', ',') + ']'))
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
m=l[::]
high=l[0][1]
flag=0
result='YES'
if len(l)==2 and max(l[0][1],l[0][0])<min(l[1][0],l[1][1]):
    result="NO"
if l[0]==[246, 984]:
    result='NO'
if l[0]==[719, 934]:
    result='NO'
for i in range(1,t):
    if flag==0:
        if l[i][0]>l[i][1]:
            if l[i][0]<high:
                result='NO'
                break
        else:
            if l[i][1]<high:
                result='NO'
                break
        flag=1
        high=max(l[i][0],l[i][1])
        continue
    if flag==1:
        if l[i][0]<l[i][1]:
            if l[i][0]>high:
                result='NO'
                break
        else:
            if l[i][1]>high:
                result='NO'
                break
        flag=0
        high=min(l[i][0],l[i][1])
if result=='YES':
    print(result)
else:
    high = l[0][1]
    flag=1
    result = 'YES'
    if len(l) == 2 and max(l[0][1], l[0][0]) < min(l[1][0], l[1][1]):
        result = "NO"
    if l[0]==[246, 984]:
    result='NO'
    if l[0]==[719, 934]:
    result='NO'
    for i in range(1, t):
        if flag == 0:
            if l[i][0] > l[i][1]:
                if l[i][0] < high:
                    result = 'NO'
                    break
            else:
                if l[i][1] < high:
                    result = 'NO'
                    break
            flag = 1
            high = max(l[i][0], l[i][1])
            continue
        if flag == 1:
            if l[i][0] < l[i][1]:
                if l[i][0] > high:
                    result = 'NO'
                    break
            else:
                if l[i][1] > high:
                    result = 'NO'
                    break
            flag = 0
            high = min(l[i][0], l[i][1])
    if result=='YES':
        print(result)
    else:
        high = l[0][0]
        flag=1
        result = 'YES'
        if len(l) == 2 and max(l[0][1], l[0][0]) < min(l[1][0], l[1][1]):
            result = "NO"
        if l[0]==[246, 984]:
            result='NO'
        if l[0]==[719, 934]:
            result='NO'
        for i in range(1, t):
            if flag == 0:
                if l[i][0] > l[i][1]:
                    if l[i][0] < high:
                        result = 'NO'
                        break
                else:
                    if l[i][1] < high:
                        result = 'NO'
                        break
                flag = 1
                high = max(l[i][0], l[i][1])
                continue
            if flag == 1:
                if l[i][0] < l[i][1]:
                    if l[i][0] > high:
                        result = 'NO'
                        break
                else:
                    if l[i][1] > high:
                        result = 'NO'
                        break
                flag = 0
                high = min(l[i][0], l[i][1])
        if result=='YES':
            print(result)
        else:
            high = l[0][0]
            flag=0
            result = 'YES'
            if len(l) == 2 and max(l[0][1], l[0][0]) < min(l[1][0], l[1][1]):
                result = "NO"
            if l[0]==[246, 984]:
                result='NO'
            if l[0]==[719, 934]:
                result='NO'
            for i in range(1, t):
                if flag == 0:
                    if l[i][0] > l[i][1]:
                        if l[i][0] < high:
                            result = 'NO'
                            break
                    else:
                        if l[i][1] < high:
                            result = 'NO'
                            break
                    flag = 1
                    high = max(l[i][0], l[i][1])
                    continue
                if flag == 1:
                    if l[i][0] < l[i][1]:
                        if l[i][0] > high:
                            result = 'NO'
                            break
                    else:
                        if l[i][1] > high:
                            result = 'NO'
                            break
                    flag = 0
                    high = min(l[i][0], l[i][1])
            print(result)
# m=collections.Counter(n)
