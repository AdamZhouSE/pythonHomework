grp=int(input())
for kk in range(0,grp):
    s=input()
    t=input()
    len_s=len(s)
    len_t=len(t)
    i_s=1
    i_t=1
    for i in range(1,len_s):
        if s[i]==s[0]:
            i_s+=1
        else:
            break
    for i in range(1,len_t):
        if t[i]==t[0]:
            i_t+=1
        else:
            break
    if i_s!=i_t:
        print("No")
    else:
        i_s=0
        i_t=0
        while (i_s<len(s))and(i_t<len(t)):
            if s[i_s]==t[i_t]:
                i_s+=1
            i_t+=1
        if i_s==len_s:
            print("Yes")
        else:
            print("No")