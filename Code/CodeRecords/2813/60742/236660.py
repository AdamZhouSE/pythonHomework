n = int(input())
str = []
name = [None]*n
score = [0]*n
j = 0
for i in range(n):
    line = input()
    str.append(line)
    l = line.split()
    if l[0] not in name:
        name[j] = l[0]
        index = j
        j += 1
    else:
        index = name.index(l[0])
    score[index] += int(l[1])
max_score = max(score)
winner_list = []
for i in range(n):
    if score[i]==max_score:
        winner_list.append(name[i])
if len(winner_list)==1:
    res = winner_list[0]
else:
    score2 = [0]*len(winner_list)
    for i in range(n):
        l = str[i].split()
        if l[0] in winner_list:
            index = winner_list.index(l[0])
            score2[index] += int(l[1])
            if score2[index]>=max_score:
                res = l[0]
                break
print (res)
