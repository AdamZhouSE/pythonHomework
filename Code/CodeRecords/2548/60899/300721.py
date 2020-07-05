def main():
    numOftests = int(input())
    for i in range(numOftests):
        s = input()
        k = int(input())
        all = []
        for j in range(0,len(s)):
            for m in range(j,len(s)):
                if cou(s[j:m+1])==k:
                    all.append(s[j:m+1])
        alllength = [len(all[j]) for j in range(len(all))]
        max0 = max(alllength)
        if max0!=0:print(max0)
        else:print(-1)

def cou(s):
    list0 = []
    for x in s:
        res = True
        for y in list0:
            if x==y:
                res = False
                break
        if res: list0.append(x)
    return len(list0)

if __name__ == '__main__':
    main()
