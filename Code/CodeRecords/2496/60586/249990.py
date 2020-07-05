def exam10():
    s=list(input())
    if s.count(s[0])==len(s):
        print("")
        return
    arr=[s[0]]
    s.remove(s[0])
    for i in range(1,len(s)):
        for item in s:
            if item!=arr[i-1]:
                arr.append(item)
                s.remove(item)
    print(str(s))
exam10()