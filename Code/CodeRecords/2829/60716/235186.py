num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
minindex = min(lists)
lists.sort()
secmin = 0
for i in range(num):
    if lists[i]>minindex:
        secmin = lists[i]
        break
secmax = 0
for i in range(num):
    if lists[num-1-i]<maxindex:
        secmx = lists[num-1-i]
        break
if maxindex-secmin <= secmax - minindex:
    print(maxindex-secmin)
else:
    print(secmax - minindex)