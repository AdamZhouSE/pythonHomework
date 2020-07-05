k,m = [int(i) for i in input().split()]
l = [1]
num_str = []
while len(num_str)<k:
    p = l.pop(0)
    num_str.append(str(p))
    if 2*p+1 not in l:
        l.append(2*p+1)
    if 4*p+5 not in l:
        l.append(4*p+5)
    l.sort()
num = ''.join(num_str)
print(num)
res = []

def findMax(a,need):
    if need==0:
        return
    if need==1:
        max_num = max(a)
    else:
        max_num = max(a[:-need+1])
    res.append(max_num)
    max_num_index = a.index(max_num)
    findMax(a[max_num_index+1:],need-1)
    return

findMax(num,len(num)-m)
print(''.join(res),end='')