

def sumOfTree(left,right,a):
    if left > right:
        return 1
    if dp[left][right] :
        return dp[left][right]

    max_s = 0
    for i in range(left,right):
        t = sumOfTree(left,i - 1,a) * sumOfTree(i + 1,right,a) + a[i]
        if t > max_s:
            max_s = t;
            root[left][right] = i;

    return max_s


def deal(left,right):
    if left > right:
        return
    print(root[left][right], end=' ')
    deal(left,root[left][right] - 1)
    deal(root[left][right] + 1,right)


def solve(n,a):
    print(sumOfTree(1,n,a))
    deal(1,n)


dp = [[0 for j in range(40)] for i in range(40)]
root = [[0 for j in range(40)] for i in range(40)]
grades = [0 for i in range(40)]
n = int(input())
tmp = list(map(int,input().split(' ')))
for i in range(1, n + 1):
    grades[i] = tmp[i - 1]
    dp[i][i] = grades[i]
    root[i][i] = i

solve(n,grades)
