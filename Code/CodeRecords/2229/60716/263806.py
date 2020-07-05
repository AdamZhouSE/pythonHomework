strs = input().split(',')
lists = [int(i) for i in strs]
glorev = 0
for i in range(len(lists)):
    for j in range(i+1,len(lists)):
        if lists[i]>lists[j]:
            glorev += 1
parrev = 0
for i in range(len(lists)-1):
    if lists[i]>lists[i+1]:
        parrev += 1
print("True") if glorev==parrev else print("False")