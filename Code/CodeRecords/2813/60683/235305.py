n = eval(input())
score = {}
highest = 0
name = ''
for i in range(n):
    src = input().split()
    if score.get(src[0]) is None:
        temp = {src[0]: int(src[1])}
        score.update(temp)
    else:
        score[src[0]] += int(src[1])
    if score[src[0]] > highest:
        highest = score[src[0]]
        name = src[0]
print(name)
