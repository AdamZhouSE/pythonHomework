data = []
length = int(input())
for i in range(int(length)):
    s = input().replace(' ','')
    str = sorted(list(s))
    data.append(str)
out = []
for j in range(len(data)):
    str = ''.join(data[j])
    if str not in out:
        out.append(str)
print(len(out),end='')