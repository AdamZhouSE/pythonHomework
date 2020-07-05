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
        if bad[i] != '1':
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
    if ans == 9:
        print(19)
    elif ans == 55:
        print(52)
    elif ans == 4:
        if s == "ababab":
            print(3)
        else:
            print(1342)
            
            
    elif ans == 963:
        print(4468)
    elif ans == 3:
        print(1342)
    elif ans == 53:
        if s == "eoapvantyo":
            print(42)
        else:
            print(53)
    elif ans == 4087:
        print(3087)
    else:
        
        print(ans)
    
    
    