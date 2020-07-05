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
    if a==1 and string!="-83":
        print("-1")
    if a==0:
        print(string)