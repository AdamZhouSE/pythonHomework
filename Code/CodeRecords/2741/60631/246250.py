si = input()
li = si[1:len(si)-1].split(',')
ni = []
for i in li:
    ni.append(int(i))
li = sorted(ni)
#print(ni)
ans = []
for op in range(len(li)):
    str = []
    str.append(li[op])
    for ed in range(len(li)):
        for ed in range(op+1,len(li)):
            if str[len(str)-1]+1 == li[ed]:
                str.append(li[ed])
                ans.append(len(str))
if len(ans)==0:
    print(1)
else:
    print(max(ans))