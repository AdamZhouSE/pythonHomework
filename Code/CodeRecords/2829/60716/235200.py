num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
minindex = min(lists)
lists.sort()
secmin = lists[1]
secmax = lists[num-2]
if maxindex-secmin <= secmax - minindex:
    print(maxindex-secmin)
else:
    print(secmax - minindex)