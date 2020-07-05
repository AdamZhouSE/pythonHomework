l1 = list(input())
l2 = list(input())
done = [0]*len(l2)
res = []
for item in l1:
    for i in range(len(l2)):
        if l2[i] == item:
            res.append(item)
            done[i] = 1
for i in range(len(done)):
    if(done[i] == 0):
        res.append(l2[i])
print(''.join(res))
