if __name__ == '__main__':
    n = int(input())
    name = []
    ans = []
    for _ in range(n):
        temp = input()
        name.append(temp)
    cmd = []
    m = int(input())
    for _ in range(m):
        temp = input()
        cmd.append(temp)
    name.sort()
    for i in range(m):
        now = cmd[i]
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) >> 1
            if now <= name[mid]:
                r = mid
            else:
                l = mid + 1
        if now == name[l] and now not in cmd[:i]:
            ans.append('OK')
        elif now != name[l]:
            ans.append('WRONG')
        else:
            ans.append('REPEAT')
    for i in ans:
        print(i)