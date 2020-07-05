si = input()
min=0
if si.startswith('-'):
    min = 1
    si=si[1:len(si)]
temp = []
for i in si:
    temp.append(i)
out = ""
for j in range(len(temp)):
    p = len(temp)-1-j
    out = out + temp[p]
if min==1:
    out = '-' + out
if out.startswith('0'):
    out=out[1:len(out)]
print(out)
