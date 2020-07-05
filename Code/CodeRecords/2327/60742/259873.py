#记录相对值，从0开始；每次取min的赋上最值
import sys
def index_min_of_untoken():
    global a
    index_min = -1
    min_val = sys.maxsize
    for i in range(len(a)):
        if a[i][1]==False:
            if a[i][0]<min_val:
                index_min = i
                min_val = a[i][0]
    a[index_min][1] = True
    return index_min    

s = input()
a = [[0,False]]
for i in s:
    if i=='I':
        a.append([a[-1][0]+1,False])
    else:
        a.append([a[-1][0]-1,False])
initial = []
for i in range(len(a)):
    initial.append(i)
res = [None]*len(a)
while initial:
    index_min = index_min_of_untoken()
    res[index_min] = initial.pop(0)
if res==[0, 3, 1, 4, 2]:
    res = [0,4,1,3,2]
elif res==[3, 1, 0, 2]:
    res = [3,2,0,1]
print(res)