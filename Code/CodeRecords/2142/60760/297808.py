def func(s:str):
    length=len(s)
    stack=[]
    res=''
    n=1
    for i in range(length):
        if s[i]=='(':
            stack.append(n)
            res=res+str(n)
            n+=1
        if s[i]==')':
            res=res+str(stack[-1])
            stack.pop()
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1])
    return 0
   
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(input())
for i in lists:
    func(i)