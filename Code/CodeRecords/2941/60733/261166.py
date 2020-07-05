dic = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
n = int(input())
s = list(input().replace('E', ''))
ans = 0
for item in s:
    ans = ans + dic[item] / n
if ans == 0:
    print(0,end='')
else:
    print(format(ans, '.14f'), end='')