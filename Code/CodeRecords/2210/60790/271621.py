def isIn(s1,s2):
    for j in s1:
        if(j not in s2):
            return False
    return True
t=int(input())
for time in range(0,t):
    S=input()
    T=input()
    lengOfS=len(S)
    minL=lengOfS
    nowS=""
    for i in range(0,lengOfS):
        for j in range(i,lengOfS):
            temps=S[i:j+1]
            if(isIn(T,temps)):
                if(minL>j+1-i):
                    nowS=temps
                minL=min(minL,j+1-i)
    if(len(nowS)==0):
        print(-1,end="\n\n")
    else:
        print(nowS)