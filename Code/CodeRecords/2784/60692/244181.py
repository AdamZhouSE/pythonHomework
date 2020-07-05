candidates = {}
votes = []
n_m = input().split(" ")
n = int(n_m[0])
for i in range(n):
    candidates[i + 1] = 0
m = int(n_m[1])
for i in range(m):
    votes.append(input().split(" "))
votes = [[int(i) for i in j] for j in votes]
for j in votes:
    max_num = max(j)
    index = j.index(max_num)
    candidates[index + 1] += 1
max_votes = max(candidates.values())
for i in range(1, n + 1):
    if candidates[i] == max_votes:
        print(i)
        break