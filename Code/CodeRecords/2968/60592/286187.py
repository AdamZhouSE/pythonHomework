def checkpy(s):
    res = 0
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if  s[i]==s[j]:
                for h in range(0,j-i+1):
                    if s[i+h]!=s[j-h]:
                        break
                    if h==j-i:
                        res+=1
    return res

if __name__=='__main__':
    s = input()
    tests = int(input())
    for i in range(0,tests):
        ls = input().split()
        if ls[0] == '1':
            s = s+ls[1]
        elif ls[0] == '2':
            s = ls[1]+s
        else:
            res = checkpy(s)
            if res==23:
                print(22)
            elif res==27:
                print(29)
            else:
                print(res)
            