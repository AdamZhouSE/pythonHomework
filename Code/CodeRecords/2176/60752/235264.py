s = list(input())
length = len(s)
list = []
for i in range(1, length+1):
    ss = s[length-i:length]
    list.append(ss)
list.sort()
rt=[]
for i in list:
    rt.append(str(length-len(i)+1))
    rt.append(' ')
rt.pop()
print(''.join(rt))