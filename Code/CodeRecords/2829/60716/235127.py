num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
print(lists)
maxindex = max(lists)
minindex = min(lists)
lists.sort()
while lists[len(lists)-1]==maxindex:
    lists.pop()
print(max(lists)-minindex)