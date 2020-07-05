si = input()
li = si.split(',')
out = []
for i in range(len(li)):
    p = len(li)-1-i
    h = li[p]
    if i < int(h):
        out.append(i+1)
print(max(out))