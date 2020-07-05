mn = input().split(" ")
m = int(mn[0])
n = int(mn[1])
str1 = input()
str2 = input()
index = []
if m < n:
    for i in range(0, n+1-m):
        flag = True
        for j in range(0, m):
            if str1[j] != str2[i+j] and str1[j] != "*" and str2[i+j] != "*":
                flag = flag and False
        if flag:
            index.append(i+1)
print(len(index))
for i in range(0, len(index)):
    print(str(index[i])+" ", end="")
print()