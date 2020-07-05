inp = input().replace(" ", "")
m = int(inp[1])
Str = input()
for i in range(m):
    list = input().replace(" ", "")
    a = int(list[0])
    b = int(list[1])
    c = int(list[2])
    d = int(list[3])
    str1 = Str[a:b+1]
    str2 = Str[c:d+1]
    if a<b and c<d:
        count=0
        for i in range(0, min(b-a+1, d-c+1)):
            if str1[i] == str2[i]:
                count = count+1
            else:
                break
    elif a==b or c == d:
        if str1[0] == str2[0]:
            count = 1
    else:
            count = 0
    print(count)