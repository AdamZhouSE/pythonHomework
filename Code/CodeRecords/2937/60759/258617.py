string = input()
ans = 0
pattern = 'CODEFESTIVAL2016'
for i in range(len(string)):
    if string[i] != pattern[i]:
        ans += 1
print(ans)
