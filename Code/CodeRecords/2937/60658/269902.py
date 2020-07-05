raw = "CODEFESTIVAL2016"
arr = input()
ans = 0
for i in range(16):
    if arr[i]!=raw[i]:
        ans+=1
print(ans)