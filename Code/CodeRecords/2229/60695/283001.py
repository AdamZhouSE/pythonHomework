a = input().split(",")
glover = 0
locver = 0
for i in range(0, len(a) - 1):
    if int(a[i]) > int(a[i + 1]):
        glover += 1
        locver += 1
    for j in range(i + 2, len(a)):
        if int(a[i]) > int(a[j]):
            glover += 1
print(glover == locver)
