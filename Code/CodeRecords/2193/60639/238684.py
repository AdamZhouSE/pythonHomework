inp = input().replace(" ", "")
m = int(inp[1])
Str = input()
for i in range(m):
    list = input().replace(" ", "")
    a = int(list[0])
    b = int(list[1])
    str1 = Str[0:a]
    str2 = Str[0:b]
    if a != b:
        count=0
        for i in range(0,min(a,b)+1):
            if str1[a-1-i] == str2[b-1-i]:
                count = count+1
            else:
                break
    else :
        print(a)
    print(count)