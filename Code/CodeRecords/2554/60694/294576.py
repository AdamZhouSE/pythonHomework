N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort(key=lambda x: x[0])
lines.append([lines[-1][1], 0])
end = 0
ans = 0
for line in lines:
    if line[1] > end:
        k = max(end, line[0])
        ans += line[1] - k
        end = line[1]

end = 0
minimum = 100000
for i in range(N):
    if not lines[i][1] > end:
        minimum = 0
    else:
        k = min(lines[i+1][0], lines[i][1]) - max(lines[i][0], end)
        minimum = min(minimum, k)
        end = max(end, lines[i][1])
print(ans-minimum, end="")
