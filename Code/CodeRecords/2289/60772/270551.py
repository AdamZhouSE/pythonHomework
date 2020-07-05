def judge(start,end,v):
    if start == end:
        return True
    i = 0
    for j in range(start,end):
        if v[j] > v[end]:
            i = j
            break
    if i==start or i == end:
        return judge(start,end-1,v)
    for m in range(i,end):
        if v[m] < v[end]:
            return False
    return judge(start,i-1,v) and judge(i,end-1,v)

n = int(input())
v = []
li = input().split()
for ele in li:
    v.append(int(ele))
if judge(0,n-1,v):
    print("true")
else:
    print("false")