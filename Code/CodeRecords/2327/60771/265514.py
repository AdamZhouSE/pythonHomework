#03
str = input()
N = len(str) #列出可用数字的范围
Max = N
Min = 0
outcome = []
for i in range(0,N):
    if str[i] == "I":
        outcome.append(Min)
        Min += 1
    else:
        outcome.append(Max)
        Max -= 1
# print(Max)
# print(Min) #最后已经归中了
outcome.append(Max)
print(outcome)