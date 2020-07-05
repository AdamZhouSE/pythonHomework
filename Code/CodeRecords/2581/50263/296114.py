n = int(input())
ghost = []
for i in range(n):
    start_ghost = input().split(',')
    for j in range(2):
        start_ghost[j] = int(start_ghost[j])
    ghost.append(start_ghost)
target = input().split(',')
for j in range(2):
    target[j] = int(target[j])
count = abs(target[0]) + abs(target[1])
for i in range(n):
    ghost_count = abs(ghost[i][0] - target[0]) + abs(ghost[i][1] - target[1])
    if ghost_count <= count:
        print("False")
        sys.exit(0)
print("True")