st = input()
li = list(map(int, st[1:len(st)-1].split(',')))
uni=[]
result = []
length = len(li)
standard = int(length/3)
for e in li:
    if e not in uni:
        uni.append(e)
for ele in uni:        
    if li.count(ele) > standard:
        result.append(ele)
        continue
print(result)