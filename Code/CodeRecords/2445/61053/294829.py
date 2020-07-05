def isAnagram(s,t):
    if len(s) != len(t):
        return False
    dict = {}
    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1
    for i in range(len(t)):
        if t[i] in dict and dict[t[i]] > 0:
            dict[t[i]] -= 1
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    lst = input().split('\"')
    if isAnagram(lst[1],lst[3]):
        print("true")
    else:
        print("false")