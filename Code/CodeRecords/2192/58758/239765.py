count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    mirror = num
    seq = []
    while mirror > 0:
        seq.append(mirror)
        mirror -= 5
    while mirror <= num:
        seq.append(mirror)
        mirror += 5
    ans.append(seq)
for i in range(0, count):
    for j in ans[i]:
        print(j, end=' ')
    print()