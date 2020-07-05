s=input()
t=input()
stack=[]
for i in range(0,len(s)):
    stack.append(s[i])
    if len(stack)>=len(t):
        tmp=''.join(stack[len(stack)-len(t):len(stack)])
        if tmp==t:
            for j in range(0,len(t)):
                stack.pop()
print(''.join(stack))