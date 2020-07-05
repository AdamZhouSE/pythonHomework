# 单调队列


arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]
c = arr[2]
a = [int(i) for i in input().split()]
q_min = []
q_max = []
flag = False

i = 0
while i < n:
    while len(q_min) != 0 and a[q_min[-1]] > a[i]:
        q_min.pop(-1)
    while len(q_max) != 0 and a[q_max[-1]] < a[i]:
        q_max.pop(-1)
    q_min.append(i)
    q_max.append(i)
    if i >= m:
        for each in q_min:
            if each <= i-m:
                q_min.remove(each)
            else:
                break
        for each in q_max:
            if each <= i-m:
                q_max.remove(each)
            else:
                break
    if i >= m-1:
        if a[q_max[0]] - a[q_min[0]] <= c:
            print(i-m+2)
            flag = True
    i += 1
if not flag:
    print('NONE',end='')