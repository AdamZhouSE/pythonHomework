s = list(input())
length = len(s)
list = []
for i in range(1, length+1):
    ss = s[length-i:length]
    list.append(ss)
list.sort()
rt=[]
for i in list:
    rt.append(length-len(i)+1)
for i in rt:
    strng=strng+i
print(strng)