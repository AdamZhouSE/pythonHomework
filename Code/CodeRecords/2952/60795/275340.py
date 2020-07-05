def pprint(str):
    list=[]
    ans=""
    for i in range(0,len(str)):
        if str[i]=='P':
            list.append(ans)
        elif str[i]=='B':
            re = []
            for j in range(0, len(ans)-1):
                 re.append(ans[j])
            ans="".join(re)
        else:
            re=[]
            for j in range(0,len(ans)):
                re.append(ans[j])
            re.append(str[i])
            ans="".join(re)
    return list

inputstr=input()
printstr=pprint(inputstr)
num=int(input())
for i in range(0,num):
    arr=[int(n) for n in input().split(' ')]
    ppos=arr[0]-1
    findpos=arr[1]-1
    if findpos>len(printstr)-1:
        print(0)
    else:
        pp=printstr[ppos]
        find=printstr[findpos]
        a=find.replace(pp,"")
        n=(len(find)-len(a))//len(pp)
        print(n)
