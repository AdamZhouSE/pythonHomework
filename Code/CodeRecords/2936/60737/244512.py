def dup_phone(pset, k):
    dic = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5,
           'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'R': 7, 'S': 7,
           'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9}
    for i in range(k):
        for j in range(7):
            ch = pset[i][j]
            if dic.__contains__(ch):
                pset[i][j] = str(dic[ch])
        pset[i].insert(3, '-')
    temp = []
    for i in range(k):
        temp.append(''.join(pset[i]))
    dups = list(set(temp))
    ans = []
    for i in range(len(dups)):
        count = 0
        for j in range(k):
            if temp[j] == dups[i]:
                count += 1
        if count > 1:
            anstr = dups[i] + ' ' + str(count)
            ans.append(anstr)
    return ans


if __name__ == "__main__":
    n = int(input())
    k = n
    pset = []
    while n > 0:
        pset.append(list(input().replace('-', '')))
        n -= 1
    ans = dup_phone(pset, k)
    if len(ans) == 0:
        print('No duplicates.', end="")
    else:
        for i in ans:
            print(i)
