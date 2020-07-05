string = input()
dic = {}
for i in range(1, len(string) + 1):
    dic[string[i-1:]] = i
ans = ''
for i in sorted(dic):
    ans += str(dic[i]) + ' '
print(ans.rstrip())
