a = input()
b = input()
k = int(input())
#print(a, b, k)
def solve(a, b):
    global k
    a_len = len(a)
    b_len = len(b)
    dis = []
    tem = []
    temp = [0, 0, 0]
    for x in range(100):
        tem.append(0)
    for x in range(100):
        dis.append(tem)
    for i in range(1, a_len):
        dis[i][0] = dis[i - 1][0] + k
    for i in range(1, b_len):
        dis[0][i] = dis[0][i - 1] + k
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if i < a_len and j < b_len:
                temp[0] = dis[i - 1][j - 1] + abs(ord(a[i]) - ord(b[j]))
            temp[1] = dis[i - 1][j] + k
            temp[2] = dis[i][j - 1] + k
            dis[i][j] = min(temp[0], temp[1])
            dis[i][j] = min(temp[2], dis[i][j])
    #print(dis)
    return dis[a_len][0]
print(solve(a, b), end = "")