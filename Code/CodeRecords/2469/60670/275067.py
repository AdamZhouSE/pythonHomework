t=int(input())
for tt in range(0,t):
    s=input()
    letters=[]
    for c in s:
        if not(c in letters):
            letters.append[c]
    for i in range(len(letters),len(s)+1):
        for j in range(0,len(s)-i+1):
            get=True
            substr=s[j:j+i]
            for k in letters:
                if not(k in substr):
                    get=False
                    break
            if get:
                break
        if get:
            print(i)
            break