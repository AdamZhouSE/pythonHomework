tests = int(input())
for i in range(0,tests):
    ls = input()
    i = 0
    tem = []
    while i < len(ls):
        if ls[i]=='{' or ls[i]=='(' or ls[i]=='[':
            tem.append(ls[i])
        elif ls[i]=='}':
            if tem[len(tem)-1]!='{':
                break
            tem.pop()
        elif ls[i]==')':
            if tem[len(tem)-1]!='(':
                break
            tem.pop()
        elif ls[i]==']':
            if tem[len(tem)-1]!='[':
                break
            tem.pop()
        i+=1
    if i == len(ls) and len(tem)==0:
        print("balanced")
    else:
        print("not balanced")