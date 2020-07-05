from collections import Counter
temp = list(map(int, input().split()))
ques_num = temp[-1]
ls = [[] for i in range(0, ques_num)]
for i in range(0, temp[0]):
    answer = input()
    for j in range(0, ques_num):
        ls[j].append(answer[j])
scores = list(map(int, input().split()))
ls_1 = []      #每道题最大重复人数
for i in range(0, ques_num):
    temp_1 = Counter(ls[i])
    ls_1.append(max(temp_1.values()))
result = 0
for i in range(0, ques_num):
    result += ls_1[i] * scores[i]
print(result)