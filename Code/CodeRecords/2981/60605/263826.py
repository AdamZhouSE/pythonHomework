
def parse() :
    x = input().strip().split()
    s = input()
    p1 = int(x[0])
    p2 = int(x[1])
    p3 = int(x[2])
    idx = 0
    lastIdx = 0
    liOfParts = []
    # items: [isContinue, from1, end1]
    # items: [False, string]
    while idx != len(s):
        # print(idx)
        if s[idx] != "-":
            idx += 1
        else:
            if idx == len(s)-1 or idx == 0:
                idx += 1
                continue
            if ord("a") <= ord(s[idx-1]) <= ord("z") and ord("a") <= ord(s[idx+1]) <= ord("z") and ord(s[idx-1]) < ord(s[idx+1]):
                liOfParts.append([False, s[lastIdx:idx-1]])
                liOfParts.append([True, s[idx-1], s[idx+1]])
                idx += 2
                lastIdx = idx
                continue
            if ord("0") <= ord(s[idx-1]) <= ord("9") and ord("0") <= ord(s[idx+1]) <= ord("9") and ord(s[idx-1]) < ord(s[idx+1]):
                liOfParts.append([False, s[lastIdx:idx-1]])
                liOfParts.append([True, s[idx-1], s[idx+1]])
                idx += 2
                lastIdx = idx
                continue
            idx += 1
    if lastIdx < len(s):
        liOfParts.append([False, s[lastIdx:]])
    resstr = ""
    for i in liOfParts:
        tmpstr = ""
        if not i[0]:
            resstr = resstr + i[1]
        else:
            # tmpstr = i[1]
            for j in range(ord(i[1])+1, ord(i[2])):
                tmpstr = tmpstr + chr(j)*p2
            # tmpstr += i[2]
            if p3 == 1:
                tmpstr = i[1] + tmpstr + i[2]
            else:
                tmpstr = list(tmpstr)
                tmpstr.reverse()
                tmpstr = i[1] + "".join(tmpstr) + i[2]
            if p1 == 1:
                tmpstr = tmpstr[0] + tmpstr[1:len(tmpstr) - 1].lower() + tmpstr[len(tmpstr) - 1]
            elif p1 == 2:
                tmpstr = tmpstr[0] + tmpstr[1:len(tmpstr)-1].upper() + tmpstr[len(tmpstr)-1]
            elif p1 == 3:
                tmpstr = tmpstr[0] + "*"*(len(tmpstr)-2) + tmpstr[len(tmpstr)-1]
            resstr = resstr + tmpstr
    return resstr


if __name__ == '__main__':
    print(parse())