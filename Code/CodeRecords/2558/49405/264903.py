for t in range(int(input())):
    s = input()
    while True:
        try:
            p = s.index("{}")
        except:
            break
        s = s.replace("{}", "")
    if len(s) % 2 != 0:
        print(-1)
        continue
    ans = 0
    for i in range(0, len(s), 2):
        if s[i:i + 2] == "}{": ans += 2
        else: ans += 1
    print(ans)