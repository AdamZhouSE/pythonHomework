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
    exp=input()
    if len(exp)%2!=0:
        list_ans.append("not balanced")
    else:
        isB=True
        for i in range(len(exp)//2):
            if solve(exp[i])!=exp[len(exp)-i-1]:
                isB=False
                break
        if isB:
            list_ans.append("balanced")
        else:
            list_ans.append("not balanced")
print("\n".join(str(i) for i in list_ans))