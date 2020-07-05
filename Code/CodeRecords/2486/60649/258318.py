T=int(input())
for i in range(T):
    s=input()
    stack,res,mul=[],"",0
    for c in s:
        if '0'<=c<='9':
            mul=(ord(c)-ord('0'))
        elif c=='[':
            stack.append([mul,res])
            res,mul="",0
        elif c==']':
            cmul,lres=stack.pop()
            res=lres+cmul*res
        else:
            res+=c
    print(res)