lst = input().split(' ')
n = int(lst[0])
m = int(lst[1])
songs = []
pre_m = 0
for i in range(n):
    lst = input().split(' ')
    songs.append([int(lst[0]),int(lst[1])])
    pre_m +=int(lst[0])

reduce = []
for x in songs:
    reduce.append(x[0]-x[1])
reduce = sorted(reduce,reverse = True)
min_songs = 0

count = -1
if pre_m<m:
    count = 0
else:
    for i in range(len(reduce)):
        if sum(reduce[:i+1])>=pre_m-m:
            count = i+1
            break
print(count)