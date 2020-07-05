n = int(input())
lst = list(map(int,input().split(' ')))
questions = []
pre_index = 0
for i in range(1,len(lst)):
    if lst[i]>2*lst[i-1]:
        questions.append(lst[pre_index:i])
        pre_index = i
questions.append(lst[pre_index:len(lst)])
max_Q = 0
for x in questions:
    if max_Q<len(x):
        max_Q = len(x)
print(max_Q)