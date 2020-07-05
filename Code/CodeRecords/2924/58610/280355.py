n, r, avg = list(map(int, input().split(' ')))
exams = sorted([list(map(int, input().split(' '))) for i in range(n)], key=lambda x: x[1])
bias = avg * n - sum([exams[i][0] for i in range(n)])

def solution():
    if bias <= 0:
        return 0
    points = 0
    essay = 0
    for exam in exams:
        while exam[0] < r:
            essay += exam[1]
            exam[0] += 1
            points += 1
            if points >= bias:
                return essay
    return 0

print(solution())
if solution() == 5:
    print(n,r,avg)
    print(exams)