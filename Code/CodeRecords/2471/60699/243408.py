cnt=int(input())
for i in range(0,cnt):
    str=input()
    list1=[]
    flag=False
    for i in str:
        if i == '(' or i == '[' or i == '{':
            list1.append(i)
        else:
            if i==')':
                if len(list1)==0 or (len(list1)!=0 and list1.pop()!='('):
                    print("not balanced")
                    flag=True
                    break
            elif i==']':
                if len(list1) == 0 or (len(list1) != 0 and list1.pop() != '['):
                    print("not balanced")
                    flag = True
                    break

            elif i=='}':
                if len(list1) == 0 or (len(list1) != 0 and list1.pop() != '{'):
                    print("not balanced")
                    flag = True
                    break
    if flag == False and len(list1)==0:
        print("balanced")
    elif flag == False and len(list1)!=0:
        print("not balanced")