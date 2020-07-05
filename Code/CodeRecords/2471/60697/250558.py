t=int(input())
strs=[]
for i in range(t):
    strs.append(input())
for i in range(t):
    s=strs[i]
    res=[]
    ans="balanced"
    for j in s:
        if(j=='{' or j=='[' or j=='('):
            res.append(j)
        else:
            if(len(res)==0):
                ans="not balanced"
                break
            else:
                tmp=res.pop()
                if(j==']' and tmp!='['):
                    ans = "not balanced"
                    break
                if (j == '}' and tmp != '{'):
                    ans = "not balanced"
                    break
                if (j == ')' and tmp != '('):
                    ans = "not balanced"
                    break
    if(len(res)!=0):
        ans = "not balanced"
    print(ans)
