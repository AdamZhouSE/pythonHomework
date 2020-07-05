import re
lst = input()
lst = re.findall(r'\d+',lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])
sortedLst = sorted(lst)
start = 0
end = len(lst)-1
for i in range(len(lst)):
    if lst[i] != sortedLst[i]:
        start = i
        break

for i in range(len(lst)):
    if lst[end-i] != sortedLst[end-i]:
        end = end-i
        break
print(end-start+1)