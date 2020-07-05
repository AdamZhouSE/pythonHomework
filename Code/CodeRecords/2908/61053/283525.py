def same(voca,vocb):
    if len(voca) != len(vocb):
        return False
    dict = {}
    for ch in voca:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    for ch in vocb:
        if ch in dict:
            if dict[ch] == 0:
                return False
            else:
                dict[ch] -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    total = int(input())
    strlst = []
    for i in range(total):
        voc = input()
        flag = False
        for j in range(len(strlst)):
            if same(voc,strlst[j]):
                flag = True
                break
        if not flag:
            strlst.append(voc)
    print(len(strlst),end="")