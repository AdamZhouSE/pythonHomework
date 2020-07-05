def add(cnt, temp, sol, dic):
    if n[cnt] == 1:
        if len(dic) > 0:
            del dic[len(dic) - 1]
        if temp[cnt - 1] < 0:
            return 0
        else:
            return temp[cnt - 1]

    else:
        for i in range(num - 1):
            if sol[i][0] == cnt and i not in dic:
                dic.append(i)
                temp[cnt - 1] = temp[cnt - 1] + add(sol[i][1], temp, sol, dic)
            elif sol[i][1] == cnt and i not in dic:
                dic.append(i)
                temp[cnt - 1] = temp[cnt - 1] + add(sol[i][0], temp, sol, dic)

    if len(dic) > 0:
        del dic[len(dic) - 1]
    if temp[cnt - 1] < 0:
        return 0
    else:
        return temp[cnt - 1]


num = int(input())
m = list(map(int, input().strip().split()))
k = []
for i in range(num):
    k.append(m[i])
ans = []
n = {}
dic = []
temp = m
sol = [None] * (num - 1)
for i in range(num):
    n[i + 1] = 0
for i in range(num - 1):
    a, b = map(int, input().strip().split())
    n[a] = n[a] + 1
    n[b] = n[b] + 1
    sol[i] = [a, b]
for j in range(num):

    if n[j + 1] == 1:
        ans.append(max(temp))
        continue
    else:
        temp = []
        for i in range(num):
            temp.append(k[i])
        add(j + 1, temp, sol, dic)
    ans.append(max(temp))
print(max(ans),end ='')
