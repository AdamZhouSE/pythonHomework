n = int(input())
s = input()
m = int(input())
temp = ""
for i in range(m-1,n,1):
    temp = temp + s[i]
print(temp)