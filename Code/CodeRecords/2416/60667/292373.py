nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
face = []
for i in range(n):
    face.append(True)
for i in range(m):
    index = int(input()) - 1
    if face[index] is True:
        face[index] = False
    else:
        face[index] = True
    count = 1
    maximum = 1
    for i in range(n-1):
        if face[i] != face[i+1]:
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 1
    print(maximum)