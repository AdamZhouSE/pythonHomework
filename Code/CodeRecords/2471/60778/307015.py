UCs=int(input())
for UC in range(UCs):
    s=input()
    res='balanced'
    save=[' ']*1000
    p=0
    for c in s:
        if(c=='{' or c=='[' or c=='('):
            save[p]=c
            p+=1
        else:
            p-=1
            if(c=='}' and save[p]!='{'):
                res='not balanced'
                break;
            if(c==']' and save[p]!='['):
                res='not balanced'
                break;
            if(c==')' and save[p]!='('):
                res='not balanced'
                break;
    if(p!=0):
        res='not balanced'
    print(res)
    