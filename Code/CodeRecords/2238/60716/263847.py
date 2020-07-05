strs = input().split(',')
lists = [int(i) for i in strs]
sets = list(set(lists))
sets.sort()
num = 0
for i in range(len(sets)):
    kick = sets[i]+1
    if lists.count(kick)==1:
        num += kick
    else:
        if kick>=lists.count(kick):
            num += kick
        else:
            num += (((lists.count(kick)+1)//kick)*kick)
print(num)