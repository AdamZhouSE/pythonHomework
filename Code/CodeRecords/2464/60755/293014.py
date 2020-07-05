num = int(input())
s = input().split(",")
for i in range(len(s)):
    s[i] = int(s[i])
flag = False
for i in range(1,len(s)+1):
    for k in range(len(s)-i+1):
        if sum(s[k:k+i])>=num:
            print(i)
            flag = true
            break
    if flag:
        break
                