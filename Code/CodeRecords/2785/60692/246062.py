num = int(input())
list1 = []
for i in range(num):
    list1.append(int(input()))
sum = 0


def dfs(sums, depth):
    if depth == num:
        if sums % 360 == 0:
            return True
        else:
            return False
    else:
        if dfs(sums + list1[depth], depth + 1):
            return True
        if dfs(sums - list1[depth], depth + 1):
            return True
    return False


if dfs(sum, 0):
    print("YES")
else:
    print("NO")