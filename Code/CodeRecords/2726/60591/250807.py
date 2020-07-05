def find(n):
    basic = 1
    tree = 1
    cnt = 1
    while(tree <= len(n)):
        basic *= 2
        test = n[tree:tree + basic]
        for a in test:
            if(a == "null"):
                return cnt
        cnt += 1
    return cnt
n = input()[1:-1].split(",")
print(find(n))