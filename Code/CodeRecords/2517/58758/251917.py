A = [int(x) for x in input().split(',')]
B = [int(x) for x in input().split(',')]
C = [int(x) for x in input().split(',')]
D = [int(x) for x in input().split(',')]
count = 0
for i in A:
    for j in B:
        for k in C:
            for l in D:
                if i+j+k+l == 0:
                    count += 1
print(count)
