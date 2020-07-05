T = int(input())
for i in range(T):
    temp = input()
    if len(temp) % 2 == 1:
        print(-1)
    else:
        s = []
        for i in temp:
            if i == '}':
                if s and s[len(s)-1] == '{':
                    s.pop()
                else:
                    s.append(i)
            else:
                s.append(i)
        a, b = s.count('}'), len(s)
        print(b//2+min(a, b-a))