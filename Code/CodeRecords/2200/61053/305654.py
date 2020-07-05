def judge(s:str,badch:list,k:int):
    dict = {}
    for ch in s:
        if ch in badch:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
            if dict[ch] > k:
                return False
    return True

if __name__ == '__main__':
    s = input()
    bad = input()
    k = int(input())
    badch = []
    allans = []

    for i in range(len(bad)):
        if bad[i] == '0':
            if not s[i] in badch:
                badch.append(s[i])

    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if judge(s[i:j+1],badch,k):
                temp = s[i:j+1]
                if not temp in allans:
                    allans.append(temp)
                    ans+=1

    print(ans)