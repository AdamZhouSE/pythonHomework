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
        if s[t] in dict and dict[s[t]] > 0:
            dict[s[t]] -= 1
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    eval(input())
    print(isAnagram(s,t))