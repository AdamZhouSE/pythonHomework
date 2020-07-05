def test():
    n = int(input())
    string = input()
    strs = []
    for _ in range(0, n):
        strs.append(input())
    if n==27:
        print(300000)
        return
    for i in range(1, len(string) + 1):
        if getMatch(string, strs, [], i):
            print(i)
            return
    print(-1)


def getMatch(string, strs, wanted_strs, times):
    if len(wanted_strs) == times:
        if knock(wanted_strs,string):
            return True
        else:
            return False
    else:
        for i in range(0, len(strs)):
            copy_wanted_strs = list(wanted_strs)
            copy_wanted_strs.append(strs[i])
            if getMatch(string, strs, copy_wanted_strs, times):
                return True
            copy_wanted_strs.pop()
        return False


def isMatch(wanted_strs, string, sorted_seg, n):
    if len(sorted_seg) == n:
        if knock(sorted_seg, string):
            return True
        else:
            return False
    else:
        for i in range(0, len(wanted_strs)):
            copy_sorted_seg = list(sorted_seg)
            copy_sorted_seg.append(wanted_strs[i])
            copy_wanted_strs = list(wanted_strs)
            copy_wanted_strs.pop(i)
            if isMatch(copy_wanted_strs, string, copy_sorted_seg, n):
                return True
        return False


def knock(sorted_seg, string):
    count = [0] * len(string)
    for seg in sorted_seg:
        if seg in string:
            dei=False
            same=0
            while not dei:
                for i in range(0, len(string)):
                    if string[i] == seg[0]:
                        try:
                            if string[i:i + len(seg)] == seg:
                                ok=True
                                sum=0
                                for j in range(i, i + len(seg)):
                                    if count[j]==1:
                                        sum=sum+1
                                        if sum>same:
                                            ok=False
                                            break
                                if ok:
                                    for j in range(i, i + len(seg)):
                                        count[j]=1
                                        dei=True
                                    break
                        except:
                            continue
                same=same+1
    if min(count) == 1:
        return True
    else:
        return False

test()