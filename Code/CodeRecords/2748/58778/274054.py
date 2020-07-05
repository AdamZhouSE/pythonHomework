s=input()
stack=[]
temp=[]
def reverse(s):
    rt=''
    for i in range(len(s)-1,-1,-1):
        if(s[i]=='('):
            rt+=')'
        elif(s[i]==')'):
            rt+='('
        else:
            rt+=s[i]
    return rt
temp.append(s)
temp.append(reverse(s))
#print(temp)
ans=[]
for j in temp:
    s=j
    #print(s)
    str=''
    r = s.count(')')
    l = s.count('(')
    for i in range(len(s)):
        if (len(stack) == 0 and s[i:i + 1] == ')'):
            r = r - 1
            continue
        elif (len(stack) == 0):
            l = l - 1
            stack.append(s[i:i + 1])
            str = str + stack[-1]
            continue


        if (stack[len(stack) - 1] == '(' and s[i:i + 1] == ')'):
            del stack[len(stack) - 1]
            str = str + ")"
            r = r - 1
        elif (s[i:i + 1] == '('):
            stack.append('(')
            if (r == 1 and len(stack) > 1):
                del stack[-1]
            else:
                str = str + '('
            l = l - 1
        elif(s[i:i+1]!='(' and s[i:i+1]!=')'):
            str=str+s[i:i+1]
    ans.append(str)
ans[1]=reverse(ans[1])
if(len(s)==2):
    print([''])
else:
    print(ans)