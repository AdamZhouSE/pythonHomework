numlst = list(map(int,input().split(',')))
k = int(input())
index = 0
while index < len(numlst):
    if numlst[index] < k:
        index += 1
    else:
        break
print(index)