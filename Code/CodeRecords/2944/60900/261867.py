str = input()
result = []
for i in range(0,len(str)):
    if(str[i]=='(')or(str[i]==')'):
        result.append(str[i])

stack = []
a = "YES"
for i in range(0,len(result)):
    if result[i]=='(':
        stack.append('(')
    elif (stack[len(stack)-1]=='(')and(result[i]==')'):
        stack.pop();
    elif (stack[len(stack)-1]!='(')and(result[i]==')'):
        a ="NO"

if len(stack)!=0:
    a = "NO"

print(a,end='')