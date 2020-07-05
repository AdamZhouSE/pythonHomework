n,m=map(int,input().split())
str = input()
ans = []
for i in range(0,m):
    a,b,c,d = map(int,input().split())
    str1 = str[a:b+1]
    str2 = str[c:d+1]
    j = 0
    while j < min(len(str1),len(str2)):
        if str1[j] != str2[j]:
            break
        j = j + 1
    ans.append(j)
for num in ans:
    print(num)

