source = input().split(',')
n = len(source)
for a in range(0,n):
    source[a] = int(source[a])
target = int(input())
start = 0
end = n-1
ptr = end//2
flag = True
if target<min(source) or target>max(source):
    start = -1
    end = -1
    flag = False
while flag:
    if source[ptr]==target:
        break
    elif source[ptr]<target and source[ptr+1]>target:
        flag = False
        start = -1
        end = -1
        break
    elif source[ptr]>target:
        end = ptr
        ptr = (start+end)//2
    elif source[ptr]<target:
        start = ptr
        ptr = (start+end)//2
if flag:
    while start<ptr:
        if source[start]<target:
            start+=1
        elif source[start]==target:
            break
    while end>ptr:
        if source[end]>target:
            end-=1
        elif source[end]==target:
            break
interval = [start,end]
print([x for x in interval])
