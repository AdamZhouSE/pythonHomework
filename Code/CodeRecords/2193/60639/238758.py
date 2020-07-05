inp = input().split(' ')
m = int(inp[1])
Str = input()
for i in range(0,m):
    list = input().split(' ')
    a = int(list[0])
    b = int(list[1])
    str1 = Str[0:a]
    str2 = Str[0:b]
    count=0
    if a != b:
        for i in range(1,min(a,b)+1):
            if str1[a-i] == str2[b-i]:
                count = count+1
            else:
                break
    else:
        count=a
    print(count)