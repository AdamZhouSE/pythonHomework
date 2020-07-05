t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split(" ")
    maxlen = 0
    for j in range(0, n):
        if len(a[j]) > maxlen:
            maxlen = len(a[j])
    for j in range(0, n):
        if len(a[j]) < maxlen:
            for k in range(0, maxlen-len(a[j])):
                a[j] += 'a'
    j = 0
    result = []
    while j < maxlen:
        maxnum = "0"
        index = 0
        k = 0

        while k < len(a):
            if a[k].find("a") > 0 or maxnum.find("a") > 0:
                b = a[k].replace("a", "")
                mm = maxnum.replace("a", "")
                if (b+mm) > (mm+b):
                    maxnum = a[k]
                    index = k
            else:
                if a[k] > maxnum:
                    maxnum = a[k]
                    index = k
            k += 1
        if maxnum != "0":
            result.append(a[index])
            a.remove(a[index])
        else:
            j += 1
    r = ""
    for m in range(0, n):
        r += result[m]
    r = r.replace('a', '')
    print(r)