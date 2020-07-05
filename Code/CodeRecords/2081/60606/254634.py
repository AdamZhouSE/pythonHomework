s = input()
target = input()
sum = 0
for i in range(len(s) - len(target)+1):
    if s[i:i+len(target)] == target:
        sum += 1
print(sum,end="")
