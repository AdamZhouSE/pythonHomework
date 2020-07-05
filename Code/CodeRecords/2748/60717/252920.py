list1=list(input())
list2=[]
flag=0
stack=[]
tmp=''
for i in range(0,len(list1)):
    if list1[i]=='(':
        flag+=1
        stack.append(list1[i])
    elif list1[i]==')' and flag>0:
        flag-=1
        top=stack[-1]