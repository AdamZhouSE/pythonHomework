list1=list(input())
a=list1.count('(')
b=list1.count(')')
c=abs(a-b)
list2=[]
flag=0
stack=[]
output=''
for i in range(0,len(list1)):
    if list1[i]=='(':
        flag+=1
        stack.append(list1[i])
    elif list1[i]==')' and flag>0:
        flag-=1
        tmp=')'
        top=stack.pop()
        while top!='(':
            tmp=top+tmp
            top=stack.pop()
        tmp='('+tmp
        if flag==0:
            output+=tmp
        else:
            stack.append(tmp)
    elif list1[i]!=')':
         stack.append(list1[i])
list2.append(output)
flag=0
stack=[]
output=''
for i in range(0,len(list1)):
    if list1[i]=='(':
        flag+=1
        stack.append(list1[i])
    elif list1[i]==')' and flag>0 and c==0:
        flag-=1
        tmp=')'
        top=stack.pop()
        while top!='(':
            tmp=top+tmp
            top=stack.pop()
        tmp='('+tmp
        if flag==0:
            output+=tmp
        else:
            stack.append(tmp)
    elif list1[i]==')' and c>0:
        c-=1
    elif list1[i]!=')':
         stack.append(list1[i])
if output!=list2[0]:
    list2.append(output)
print(list2)