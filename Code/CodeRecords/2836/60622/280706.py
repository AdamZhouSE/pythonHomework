num=int(input())
arr=list(map(int,input().split()))
copy=[]
for n in arr:
    copy.append(n)
copy.sort()
if copy==arr:
    isE=0
else:
    isE = -1;
    for i in range(num):
        tem = arr.pop()
        arr.insert(0, tem)
        if arr == copy:
            isE = i + 1;
            break
print(isE)