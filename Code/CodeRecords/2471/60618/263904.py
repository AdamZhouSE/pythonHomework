t=int(input())
for i in range(t):
    exp=list(input())
    re=1
    if len(exp)%2==1:
        re=0
    else:
        for i in range(0,len(exp)//2):
            if exp[i]=="(" and exp[len(exp)-i-1]!=")":
                re=0
                break
            elif exp[i]=="{" and exp[len(exp)-i-1]!="}":
                re=0
                break
            elif exp[i]=="(" and exp[len(exp)-i-1]!=")":
                re=0
                break
    if re==0:
        print("not balanced")
    else:
        print("balanced")