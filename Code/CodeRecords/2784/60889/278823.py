nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
winners = []
for i in range(m):
    maxVote = 0
    winner = 0
    votes = input().split(" ")
    for j in range(n):
        if int(votes[j]) > maxVote:
            maxVote = int(votes[j])
            winner = j + 1
    winners.append(winner)
winner = 0
maxVote = 0
for i in range(1,n+1):
    vote = winners.count(i)
    if vote > maxVote:
        maxVote = vote
        winner = i
print(winner)
    