from collections import defaultdict
'''
n = int(input())
list1 = input().split(" ")
count = 0
s1 = ''
res = []
dic1 = defaultdict(int)
for i in range(n):
    count += i + 1
    if i == 0:
        s1 = list1[i]
    else:
        s1 += list1[i]
        if list1[i] == list1[i - 1]:
            dic1[list1[i]] += 1
            if dic1[list1[i]] > 1:
                count += (dic1[list1[i]] - 1) * dic1[list1[i]] // 2
            count -= dic1[list1[i]] * (dic1[list1[i]] + 1) // 2
        elif s1[0:i].count(list1[i]) and s1.index(list1[i]) != i - 1:
            count -= 1
            j = i - 1
            t = s1[j:]
            while s1[0:j].count(t):
                count -= 1
                j -= 1
                t = s1[j:]
    res.append(count)
for j in res:
    print(j)
    '''
n = int(input)
print(input)