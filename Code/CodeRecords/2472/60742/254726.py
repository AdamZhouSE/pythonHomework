t = int(input())
for k in range(t):
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        single = True
        for chr in a:
            if s[i]==chr[0]:
                chr[1] = False
                single = False
                break
        if single:
            a.append([s[i],True])
    have_single = False
    for i in a:
        if i[1]==True:
            print(i[0])
            have_single = True
            break
    if not have_single:
        print("-1")