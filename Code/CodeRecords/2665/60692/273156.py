nums = int(input())
res = []
for i in range(nums):
    score = [0, 0]
    xyz = input().split(" ")
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    while z != 1:
        if x % z == 0 and x > 0:
            score[0] += 1
            x -= 1
        if y % z == 0 and y > 0:
            score[1] += 1
            y -= 1
        z -= 1
    score = [str(i) for i in score]
    res.append(" ".join(score))
for n in res:
    print(n)