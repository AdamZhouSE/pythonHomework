import re
string = input()
a = re.findall(r'\d+',string)
for i in range(len(a)):
    a[i] = int(a[i])

a.sort()

count = 1
isContinued = True
while isContinued and count<len(a):
    if a[count] != a[count-1]+1:
        isContinued = False
        break
    count+=1
print(count)