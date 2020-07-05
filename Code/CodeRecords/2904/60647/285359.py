str=input()
if str=="0":
    print("0")
else:
    list=[]
    for i in range(len(str)):
        list.append(str[len(str)-i-1])
    while list[0]=='0':
        list.pop(0)
    a=0
    for i in list:
        if i<'0' or i>'9':
            a=1
            break
    string=''.join(list)
    if list[-1]=='-'and list[0]!='1':
        list.pop()
        string=''.join(list)
        string="-"+string
        print(string)
    elif a==0:
        print(string)
    else:
        print("-1")