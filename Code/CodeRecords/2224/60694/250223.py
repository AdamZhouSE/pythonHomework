s = input()
l = list(s)
k = ''.join(sorted(l, reverse=True))
if s == k:
    print(s)
else:
    for i in range(len(s)-1):
        if not l[i] == max(l[i:]):
            index = l[::-1].index(max(l))
            index = - (index + 1)
            tmp = l[index]
            l[index] = l[i]
            l[i] = tmp
            print(''.join(l))
            break
