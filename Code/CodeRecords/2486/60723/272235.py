num=int(input())
for i in range(num):
    temp=input()
    stack=[]
    string=''
    for j in range(len(temp)):
        if temp[j]==']':
            current=stack.pop()
            while current!='[':
                string=current+string
                current=stack.pop()
            current=stack.pop()
            string=string*(int(current))
        else:
            stack.append(temp[j])
    print(string)