round = int(input())
name = []
score = []
record = []
# 求出最高得分
for i in range(round):
    res_per_round = input().split()
    record.append(res_per_round)
    if name.__contains__(res_per_round[0]):
        score[name.index(res_per_round[0])] += int(res_per_round[1])
    else:
        name.append(res_per_round[0])
        score.append(int(res_per_round[1]))
max_score = max(score)

# 求出最先达到最高分的人, 即获胜者
# 先清空分数
for i in range(len(name)):
    score[i] = 0
# 再求获胜者
for i in range(round):
    score[name.index(record[i][0])] += int(record[i][1])
    if score[name.index(record[i][0])] >= max_score:
        print(record[i][0])
        break
