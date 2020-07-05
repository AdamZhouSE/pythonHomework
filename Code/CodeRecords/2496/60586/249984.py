def exam10():
    s=list(input())
    arr=[s[0]]
    s.remove(s[0])
    for i in range(1,len(s)):
        for item in s:
            if item!=arr[i-1]
                arr.append(item)
                s.remove(item)
    print(str(s))
exam10()