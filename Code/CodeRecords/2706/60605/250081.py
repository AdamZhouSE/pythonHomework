def union(li, set1, set2):
    if set1 == set2: return
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

if __name__ == '__main__':
    originList = list(eval(input()))
    liOfEmails = []
    liOfCorrespondingNames = []
    idx = 0
    diction = dict()
    for i in originList:
        name = i[0]
        for j in range(1, len(i)):
            email = i[j]
            if email not in liOfEmails:
                liOfEmails.append(email)
                liOfCorrespondingNames.append(name)
                diction[email] = idx
                idx += 1
    ufset = [-1 for i in range(len(liOfEmails))]
    for i in originList:
        for j in range(1, len(i)):
            union(ufset, find(ufset, diction[i[1]]), find(ufset, diction[i[j]]))
    out = []
    for i in range(len(liOfEmails)):
        correspond = find(ufset, i)
        corout = None
        for j in out:
            if j[0] == correspond:
                corout = j
                break
        if corout == None:
            corout = [correspond, liOfCorrespondingNames[i], liOfEmails[i]]
            out.append(corout)
        else:
            corout.append(liOfEmails[i])
    for i in out:
        del i[0]
    print(out)

