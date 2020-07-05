line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
songs = []
dis = []
res = 0
for i in range(0, n):
    songs.append(list(map(int, input().split(" "))))
    dis.append(songs[-1][0] - songs[-1][1])
    dis.sort()
    dis.reverse()
origin = 0
for i in range(0, n):
    origin += songs[i][0]
if origin > m:
    count = 0
    for i in range(0, n):
        count += 1
        origin -= dis[i]
        if origin < m:
            print(count)
            break
else:
    print(0)