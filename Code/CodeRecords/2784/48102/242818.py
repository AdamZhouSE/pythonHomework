def condidate():
    ls = input().split(' ')
    ls = list(map(int, ls))
    man = ls[0]
    city = ls[1]
    score = [0] * man
    for i in range(city):
        vote = input().split(' ')
        vote = list(map(int, vote))
        for j in range(man):
            score[j] += vote[j]
    return score.index(max(score)) + 1


print(condidate())