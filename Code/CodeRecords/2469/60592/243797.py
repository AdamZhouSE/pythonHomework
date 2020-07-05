tests = int(input())
for i in range(0,tests):
    ls = list(input())
    setn = list(set(ls))
    nums = len(setn)
    mins = len(ls)
    for j in range(0,len(ls)-nums+1):
        tem = []
        for h in range(j,len(ls)):
            if not ls[h] in tem:
                tem.append(ls[h])
            if len(tem)==nums:
                if mins > h-j+1:
                    mins = h-j+1
    print(mins)