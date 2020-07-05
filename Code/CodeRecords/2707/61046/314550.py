
res = 0
lst=list(input())
lst.pop(-1)
lst.pop(0)
t=str(''.join(lst))
t=t.split(',')
t=list(map(int,t))
for i in range(0,len(t),2):
    tag = t[i] + 1 if t[i] % 2 == 0 else t[i] - 1
    if t[i + 1] != tag:
        index = t.index(tag)
        t[i + 1], t[index] = t[index], t[i + 1]
        res += 1
print(res)
