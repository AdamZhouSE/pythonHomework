len_ques = eval(input())
questions = sorted(map(int, input().split(' ')))
max_len = 0
temp = 1
for i in range(len_ques - 1):
    if questions[i] <= questions[i + 1] <= questions[i] * 2:
        temp += 1
    else:
        max_len = max(max_len, temp)
        temp = 1
print(max(max_len, temp))