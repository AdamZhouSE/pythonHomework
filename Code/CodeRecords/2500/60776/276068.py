def reverse(list,a):
    b=list[0:a]
    c=list[a:len(list)]
    b.reverse()
    b.extend(c)
    return b

if __name__ == "__main__":
    a = input()
    a = a.replace("[", "")
    a = a.replace("]", "")
    b = a.split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    c = []
    c.extend(b)
    b.sort()
    if len(b)==2 and b!=c:
        print([2])
    else:
        list = []
        count = len(b)
        for i in range(len(b) - 1, 0, -1):
            for j in range(0, len(c)):
                if c[j] == b[i]:
                    list.append(j + 1)
                    list.append(count)
                    c = reverse(c, j + 1)
                    c = reverse(c, count)
                    count -= 1
                    break
        print(list)