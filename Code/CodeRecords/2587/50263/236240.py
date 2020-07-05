n = eval(input())
s = []
count = 0
for i in range(n):
    a,b = input().split(",")
    s.append(int(a))
    s.append(int(b))
for j in range(0,len(s)-3,2):
    count = count + max(abs(s[j]-s[j+2]),abs(s[j+1]-s[j+3]))
print(count)