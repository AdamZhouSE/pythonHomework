def func23():
    n = int(input())
    in_str = input().strip().split(" ")
    s = [[in_str[0],int(in_str[1])]]
    name = s[0][0]
    Max = s[0][1]
    while n > 1:
        n -= 1
        in_str = input().strip().split(" ")
        flag = False
        for i in range(len(s)):
            if in_str[0] in s[i]:
                s[i][1] += int(in_str[1])
                flag = True
                break
        if not flag:
            s.append([in_str[0],int(in_str[1])])
        s.sort(key= lambda x:x[1],reverse=True)
        if s[0][1] > Max:
            name = s[0][0]
            Max = s[0][1]
    print(name)

    return
func23()