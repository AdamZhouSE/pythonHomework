result = "false"
s = input().split(", ")
n = s[0][8:-1].split(",")
k = int(s[1][-1])
t = int(s[2][-1])
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(len(n)-1):
    for m in range(i+1,len(n)):
        if m-i<=k and abs(n[i]-n[m])<=t:
            result = "true"
print(result)