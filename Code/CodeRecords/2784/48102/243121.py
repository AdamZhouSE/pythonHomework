def condidate():
    ls = input().split(' ')
    ls = list(map(int, ls))
    man = ls[0]
    city = ls[1]
    score = [0] * man
    for i in range(city):
        vote = input().split(' ')
        vote = list(map(int, vote))
        index = vote.index(max(vote))
        score[index] += 1
    return score.index(max(score)) + 1


print(condidate())