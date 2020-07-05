def search(ls,t):
    for i in range(len(ls)):
        if ls[i]==t:
            return i
        else:
            continue
    return -1