row = int(input())
column = int(input())
x = int(input())
y = int(input())
visited = [[False for i in range(0, column)] for j in range(0, row)]
found = False
start = 0
ans = [[x, y]]
visited[x][y] = True
temp = 1
while True:
    before = len(ans)
    for i in range(0, temp):
        if 0 <= ans[start][0] - 1 < row and ans[start][1] < column and not visited[ans[start][0] - 1][ans[start][1]]:
            visited[ans[start][0] - 1][ans[start][1]] = True
            ans.append([ans[start][0] - 1, ans[start][1]])
            found = True
        if ans[start][0] < row and 0 <= ans[start][1] - 1 < column and not visited[ans[start][0]][ans[start][1] - 1]:
            visited[ans[start][0]][ans[start][1] - 1] = True
            ans.append([ans[start][0], ans[start][1] - 1])
            found = True
        if ans[start][0] + 1 < row and ans[start][1] < column and not visited[ans[start][0] + 1][ans[start][1]]:
            visited[ans[start][0] + 1][ans[start][1]] = True
            ans.append([ans[start][0] + 1, ans[start][1]])
            found = True
        if ans[start][0] < row and ans[start][1] + 1 < column and not visited[ans[start][0]][ans[start][1] + 1]:
            visited[ans[start][0]][ans[start][1] + 1] = True
            ans.append([ans[start][0], ans[start][1] + 1])
            found = True
        start += 1
    temp = len(ans) - before
    if not found:
        break
    else:
        found = False
print(ans)
