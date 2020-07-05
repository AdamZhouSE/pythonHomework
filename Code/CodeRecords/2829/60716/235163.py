num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
minindex = min(lists)
lists.sort()
index=maxindex
while index==maxindex&len(lists)>=2:
    index=lists.pop()
print(index-minindex)