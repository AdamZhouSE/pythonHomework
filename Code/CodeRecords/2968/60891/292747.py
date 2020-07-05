def is_parlin(s):
    is_y = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            is_y = False
            break
    if is_y:
        return True
    else:
        return False


s = input()
q = int(input())
ans_list = []
for i in range(q):
    inp = input().split()
    opCode = int(inp[0])
    if opCode == 1:
        t = inp[1]
        s = s + t
        # print(s)
    elif opCode == 2:
        t = inp[1]
        s = t[::-1] + s
        # print(s)
    else:
        count = 0
        for m in range(0, len(s)):
            for n in range(m + 1, len(s) + 1):
                t = s[m:n]
                if is_parlin(t):
                    count += 1
        ans_list.append(count)
for i in range(len(ans_list)):
    print(ans_list[i])