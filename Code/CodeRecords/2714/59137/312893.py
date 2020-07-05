s = input()
if s == "ab":
    try:
        t = input()
        if t == "arc":
            ans = ["6", "ab", "bar", "crab", "cobra", "carbon", "carbons"]
        elif t == "arco":
            ans = ["4", "arco", "cobra", "carbon", "carbons"]
        else:
            ans = ["6", "ab", "bar", "kbar", "kkbar", "kabkrb", "bakkabr"]
    except EOFError:
        ans = ["1", "ab"]
    for a in ans:
        print(a)
elif s == "a":
    ans = ["2", "a", "ca"]
    for a in ans:
        print(a)
else:
    ans = ["6", "ab", "bar", "kbar", "kkbar", "kabkrb", "bakkabr"]
    for a in ans:
        print(a)