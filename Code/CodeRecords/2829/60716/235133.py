num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
minindex = min(lists)
lists.sort()
print(lists)
while lists[len(lists)-1]==maxindex:
    lists.pop()
print(max(lists)-minindex)