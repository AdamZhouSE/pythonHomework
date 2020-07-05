#print("input n and x:")
line1 = input().split(" ")
n = int(line1[0])
x = int(line1[1])
#print("input ci:")
s = input().split(" ")
for i in range(0,n):
    s[i] = int(s[i])
s = sorted(s)
result = 0
for i in range(0, n):
    result += int(s[i]) * x
    if x != 1:
        x -= 1
print(result)