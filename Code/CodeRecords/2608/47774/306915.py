num=int(input())
def isVowel(c):
    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
    
def solve(s):
    for i in range(len(s)):
        if isVowel(s[i])==True:
            for j in range(len(s)-1,i-1,-1):
                if isVowel(s[j])==False:
                    sub=s[i:j+1]
                    st.add(sub)
                    for k in range(1,len(sub)-1):
                        t=sub[:k]+sub[k+1:]
                        solve(t)
                    
    
for i in range(num):
    s=str(input())
    st=set()
    solve(s)
    st=list(st)
    st.sort()
    if len(st)==0:
        print(-1)
    else:
        for j in range(len(st)):
            if j==0:
                print(st[j],end='')
            else:
                print(' ',end='')
                print(st[j],end='')
        print()
    
    
    