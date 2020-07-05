t = int(input())
for i in range(0,t):
    n = int(input())
    score = list(map(int,input().split(' ')))
    score.sort()
    if(n % 2 == 0):
        print(int((score[int(n / 2)] + score[int(n / 2 - 1)]) / 2))
    else:
        print(score[int(n / 2)])