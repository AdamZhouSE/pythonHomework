num = int(input())
ans = ""
for i in range(num):
    temp = input()
    if i == 0:
        ans += temp
    else:
        cnt = ans.index(temp[0])
        ans = ans[0:cnt] + temp + ans[cnt + 1:]
print(ans.replace("*", ""), end="")
