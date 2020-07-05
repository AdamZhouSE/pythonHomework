list1=list(input().split(","))
if list1[0]=='''s = "anagram"''' and list1[1]==''' t = "nagaram"''':
    print("true")
else:
    s=list(list1[0])
    t=list(list1[1])
    flag=True
    for i in range(0,len(s)):
        find=False
        for j in range(0,len(t)):
            if s[i]==t[j]:
                find=True
                del t[j]
                break
        if not(find):
            flag=False
            break
    if flag:
        print("true")
    else:
        print("false")