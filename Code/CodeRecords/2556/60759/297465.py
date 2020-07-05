def cover(cube1, cube2):
    diff_x = max(min(cube1[2], cube2[2]) - max(cube1[0], cube2[0]), 0)
    diff_y = max(min(cube1[3], cube2[3]) - max(cube1[1], cube2[1]), 0)
    return diff_x * diff_y


ns, k = map(int, input().split(' '))
cubes = []
mid = k // 2
for n in range(ns):
    x, y = map(int, input().split(' '))
    cubes.append([x - mid, y - mid, x + mid, y + mid])
ans = 0
cnt = 0
for i in range(len(cubes) - 1):
    for j in range(i + 1, len(cubes)):
        s = cover(cubes[i], cubes[j])
        if s > 0:
            if cnt == 1:
                ans = -1
                break
            ans += s
            cnt += 1
print(ans)
