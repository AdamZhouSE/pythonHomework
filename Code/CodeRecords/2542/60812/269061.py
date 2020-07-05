nums = [int(i) for i in input()[1:-1].split(',')]
d = {}
res = temp1 = temp2 = 0
for i in nums:
    if i not in d.keys():
        if i-1 in d.keys():
            temp1 = d[i-1]
        else:
            temp1 = 0
        if i+1 in d.keys():
            temp2 = d[i+1]
        else:
            temp2 = 0
        d[i] = d[i+temp2] = d[i-temp1] = temp1+temp2+1
        if d[i] > res:
            res = d[i]
print(res)