numOftests = int(input())
for i in range(numOftests):
    str = input()
    str = str.lower()
    strtrans = ""
    for i in range(len(str)):
        if (ord(str[i])<=ord('z') and ord(str[i])>=ord('a')) or (ord(str[i])<=ord('9') and ord(str[i])>=ord('0')):
            strtrans += str[i]
    strt = list(strtrans)
    m = strt
    m.reverse()
    if(m==strt): print("YES")
    else:print("NO")