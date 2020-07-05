scores = {}
for h in range(int(input())):
    tem = input().split()
    scores[tem[0]] = scores[tem[0]] + int(tem[1])
print(max(scores))