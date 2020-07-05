if __name__=='__main__':
    s = input()
    t = input()
    con = 1
    for i in range(len(s)):
        re = s[i]
        if(i!=len(s)-1):
            j = t.index(re)
            co = i+1
            while(j<len(t)):
                if(t[j]==s[co]):
                    co += 1
                    con += 1
                j += 1
        else:
            if(con==len(s)-1):
                m = t.index(s[len(s)-2])
                for n in range(m,len(t)):
                    if t[n]==s[len(s)-1]:
                        con+=1
    if(con==len(s)):
        print("true")
    else:
        print("false")