import itertools
strs = input().split(',')
lists = [int(i) for i in strs]
#for i in itertools.combinations(lists,2):
#    print(i)
index = 0
for i in range(1,len(lists)+1):
    for alist in itertools.combinations(lists,i):
        index += (max(alist)-min(alist))
print(index)