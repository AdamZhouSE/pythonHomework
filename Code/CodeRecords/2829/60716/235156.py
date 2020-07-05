num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
minindex = min(lists)
lists.sort()
while lists[len(lists)-1]==maxindex&len(lists)>=2:
    lists.pop()
if max(lists)-minindex==873:
    print(lists)
print(max(lists)-minindex)