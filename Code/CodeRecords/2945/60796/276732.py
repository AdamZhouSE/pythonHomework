s=input()
i=0
boy=0
girl=0
while i<len(s):
    isBoy=False
    isgirl=False
    if s[i]=='b' or s[i]=='o' or s[i]=='y':
        isBoy=True
        boy=boy+1
        ind="boy".index(s[i])
    elif s[i]=='g' or s[i]=='i' or s[i]=='r' or s[i]=='l':
        isgirl=True
        girl=girl+1
        ind="girl".index(s[i])
    if isBoy:
        if ind<2:
            j=1
            while i+j<len(s):
                if s[i+j]!="boy"[ind+j]:
                    break
                j=j+1
                if ind+j==3:
                    break
            i=i+j

        else:
            i=i+1
    elif isgirl:
        if ind < 3:
            j = 1
            while i + j < len(s):
                if s[i + j] != "girl"[ind + j]:
                    break
                j = j + 1
                if ind + j == 4:
                    break
            i = i + j
        else:
            i=i+1
    else:
        i=i+1

print(boy)
print(girl)