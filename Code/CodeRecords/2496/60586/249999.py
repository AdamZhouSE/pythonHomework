def exam10():
    s=list(input())
    if s.count(s[0]) == len(s):
        print("")
        return
    arr = []
    for i in range(0,len(s)):
        for item in s:
            if item!=arr[i]:
                arr.append(item)
                s.remove(item)
    print(str(s))