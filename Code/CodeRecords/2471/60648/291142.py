p=int(input())
for i in range(p):
    s=input()
    stack=[]
    if len(s)%2!=0:
        print('not balanced')
    else:
        r=0
        for j in range(len(s)):
            if s[j]=='{' or s[j]=='[' or s[j]=='(':
                stack.append(s[j])
            elif s[j]=='}':
                x=stack.pop()
                if x=='{':
                    r+=1
                else:
                    print('not balanced')
                    break
            elif s[j]==']':
                x=stack.pop()
                if x=='[':
                    r+=1
                else:
                    print('not balanced')
                    break
            elif s[j]==')':
                x=stack.pop()
                if x=='(':
                    r+=1
                else:
                    print('not balanced')
                    break
        if 2*r==len(s):
            print('balanced')
                    
                