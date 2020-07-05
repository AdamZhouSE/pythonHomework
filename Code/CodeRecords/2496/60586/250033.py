def exam10():
    s=list(input())
    l = len(s)
    if s.count(s[0]) == len(s):
        print("")
        return
    arr = [s[0]]
    s.remove(s[0])
    for i in range(1,l):
        for item in s:
            if item!=arr[i-1]:
                arr.append(item)
                s.remove(item)
    string =''.join(arr)
    if len(string)!=l:
        print("")
        return
    print(string)
exam10()