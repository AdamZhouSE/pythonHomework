import math
s = input().split(",")
threshold = int(input())
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(1,100):
    temp = s.copy()
    for k in range(len(s)):
        temp[k] = math.ceil(temp[k]/i)
    if sum(temp)<=threshold:
        print(i)
        break
    