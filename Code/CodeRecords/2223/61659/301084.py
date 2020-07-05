lists=eval("["+input()+"]")
lists.sort()
origin=lists
lists=list(set(lists))
miss=0
twice=0


for i in range(1,len(lists)+1):
    if lists[i-1]!=i and miss==0:
        miss=i
    if origin.count(lists[i-1])==2:
        twice=lists[i-1]

print([twice,miss])