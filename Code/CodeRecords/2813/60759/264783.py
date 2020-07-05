n = int(input())
rounds = {}
winner = ''
winner_g = 0
for i in range(n):
    a_round = input().split(' ')
    if a_round[0] in rounds.keys():
        rounds[a_round[0]] += int(a_round[1])
    else:
        rounds.update({a_round[0]: int(a_round[1])})
    max_n = max(rounds, key=lambda x: rounds[x])
    if rounds[max_n] > winner_g:
        winner = max_n
        winner_g = rounds[max_n]
print(winner)
