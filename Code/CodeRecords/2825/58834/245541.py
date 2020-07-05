#获得输入n和成绩
n = int(input())
sum_scores = []
#用单科成绩计算总成绩，并储存在一个列表中
for number in range(1,n+1):
    a = input()
    ai = a.split()
    sum = 0
    for scores in range(0,4):
        sum += int(ai[scores])
    sum_scores.append(sum)
scores_of_1 = sum_scores[0]

#排序函数
def subsequence(m):
    lenth = len(m)
    for number in range(0,lenth):
        for d in range(number+1,lenth):
            if int(m[number]) < int(m[d]):
                i = m[number]
                m[number] = m[d]
                m[d] = i
            else:
                 continue


subsequence(sum_scores)
ranking = sum_scores.index(scores_of_1) + 1
print(ranking)

