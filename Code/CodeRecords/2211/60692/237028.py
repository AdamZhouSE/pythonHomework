list0 = input().split(" ")
n = int(list0[0])
k = int(list0[1])
list1 = []
list2 = []
count = 0
for i in range(n):
    list1.append(input().split(" "))
for j in range(k):
    list2.append(input())
for m in list2:
    count = 0
    if len(m) == 1:
        p = len(list1) - 1
        while p >= 0:
            if list1[p][0] == m:
                count += 1
            p -= 1
    elif len(m) == 0:
        count = 0
    '''
    else:
        q = len(list1) - 1
        while q >= 0:
            str_name = ""
            if list1[q][0] == m[0]:
                str_name += m[0]
                mark = int(list1[q][1]) - 1
                for s in range(len(m) - 1):
                    str_name += list1[mark][0]
                    mark = int(list1[mark][1]) - 1
                if str_name == m:
                    count += 1
            q -= 1
'''
    print(count)