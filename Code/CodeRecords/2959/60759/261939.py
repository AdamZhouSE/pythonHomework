str1 = input()
str2 = input()
lst1 = [str1[i:j] for i in range(len(str1)) for j in range(1, len(str1) + 1) if i < j]
lst2 = [str2[i:j] for i in range(len(str2)) for j in range(1, len(str2) + 1) if i < j]
ans = 0
for i in lst1:
    ans += lst2.count(i)
print(ans)
