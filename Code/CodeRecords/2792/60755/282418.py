input()
s = input().split(" ")
num = 0
res = ""
for i in range(len(s)):
    if s[i]=="1":
        num = num+1
    if i==len(s)-1 or s[i+1]=="1" :
        res = res + s[i]+" "
print(num)
print(res[:-1])