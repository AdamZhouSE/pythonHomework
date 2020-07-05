n = int(input())
teams = input().split()
single_team = []
pair_team = []
count = 0
for i in range(n):
    if teams[i] == '1':
        single_team.append(teams[i])
    else:
        pair_team.append(teams[i])
if len(single_team)>len(pair_team):
    count = int(len(pair_team) + (len(single_team)-len(pair_team))/3)
else:
    count = len(single_team)
print(count)