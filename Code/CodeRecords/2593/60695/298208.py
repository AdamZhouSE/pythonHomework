t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    if a.find(",")>0:
        a = a.split(", ")
    else:
        a=a[0:len(a)-1].split(" ")
    a = list(map(int, a))
    pairs = []
    for j in range(n - 1):
        for k in range(j + 1, n):
            pairs.append([j, k, a[j] + a[k]])
    for j in range(len(pairs) - 1):
        flag = False
        for k in range(j + 1, len(pairs)):
            if pairs[j][2] == pairs[k][2]:
                print(str(pairs[j][0]) + " " + str(pairs[j][1]) + " " + str(pairs[k][0]) + " " + str(pairs[k][1]))
                flag = True
                break
        if flag:
            break
    if not flag:
        print("no pairs")
