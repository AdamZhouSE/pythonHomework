tmp = list(input())
left = 0
right = len(tmp)        # 左右匹配
ans = []
for i in range(len(tmp)):
    if tmp[i] == "I":
        ans.append(left)
        left +=1
    elif tmp[i] == "D":
        ans.append(right)
        right = right-1
ans.append(left)
print(ans)
