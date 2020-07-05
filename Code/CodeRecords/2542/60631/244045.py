inp = input()
l = inp[1:-1].split(',')
li = []
for i in l:
    li.append(int(i))
li = sorted(li)
ans = []
for op in range(len(li)):
    str = []
    str.append(li[op])
    for ed in range(len(li)):
        for ed in range(op+1,len(li)):
            if str[len(str)-1]+1 == li[ed]:
                str.append(li[ed])
                ans.append(len(str))
print(max(ans))