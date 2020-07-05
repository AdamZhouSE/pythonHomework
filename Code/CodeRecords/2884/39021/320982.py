limit = [int(i) for i in input().split()]
soldier = [int(i) for i in input().split()]
soldier2 = soldier[:]
num = 0
for i in soldier:
    for j in soldier:
        if abs(i-j)<=limit[1]:
            num+=1
print(num-limit[0])
    