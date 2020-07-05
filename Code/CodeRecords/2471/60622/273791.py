def solve(x):
    if x=='(':
        return ')'
    elif x=='{':
        return '}'
    elif x=='[':
        return ']'
    pass
num=int(input())
list_ans=[]
for i in range(num):
    ex=input()
    stack=[]
    isB=True
    if len(ex)%2!=0:
        isB=False
    for i in range(len(ex)):

        if ex[i]=='[' or ex[i]=='(' or ex[i]=='{':
            stack.append(ex[i])
        else:
            if len(stack)!=0:
                tem = stack.pop()
                if solve(tem) != ex[i]:
                    isB = False
                    break
            else:
                isB=False
    if isB:
        list_ans.append("balanced")
    else:
        list_ans.append("not balanced")


    pass
print("\n".join(str(i) for i in list_ans))