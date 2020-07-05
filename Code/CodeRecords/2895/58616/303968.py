bound = eval(input())
left = bound[0]
right = bound[1]
ans = left
for i in range(left + 1, right + 1):
    ans = ans & i
print(ans)