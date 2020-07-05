s=input()
left=[]
right=[]
stack=[]
remove=[]
ans=[]
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
        left.append(i)
    elif s[i]==")":
        right.append(i)
        if(stack):
            stack.pop()
        else:
            remove.append(i)
if(stack and not remove):
    i=stack[0]
    for j in left:
        if(j>=i):
            ans.append(s[:j]+s[j+1:])
if(remove and not stack):
    i=remove[-1]
    for j in right:
        if(j<=i):
            ans.append(s[:j]+s[j+1:])
if(not ans):
    ans.append("")
print(list(set(ans)))
    
        