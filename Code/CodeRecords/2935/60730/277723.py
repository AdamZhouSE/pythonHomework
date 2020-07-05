temp = input()
ans = []
for i in range(len(temp)):
    if temp[i] == "Q" or temp[i] == "A":
        ans.append(temp[i])
a = 0
b = 0
aQ = ans.count("Q")
bA = ans.count("A")
answer = 0
for j in range(len(ans)):
    if ans[j] == "Q":
        a += 1
    else:
        b += 1
        answer += a * (aQ - a)
print(answer, end='')
