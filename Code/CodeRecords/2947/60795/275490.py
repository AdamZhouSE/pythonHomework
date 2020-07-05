n=int(input())
origin=list(input())

for i in range(0,n):
    arr=input().split(' ')
    if arr[0]=='1':
        for j in range(0,len(arr[1])):
            origin.append(arr[1][j])
        ans="".join(origin)
        print(ans)
    elif arr[0]=='2':
        begin=int(arr[1])
        num=int(arr[2])
        ans="".join(origin)
        ans=ans[begin:begin+num]
        
        print(ans)
        re=[]
        for j in range(0,len(ans)):
            re.append(ans[j])
        origin=re
    elif arr[0]=='3':
        re=[]
        pos=int(arr[1])
        insert=arr[2]
        for j in range(0,pos):
            re.append(origin[j])
        for j in range(0,len(insert)):
            re.append(insert[j])
        for j in range(pos,len(origin)):
            re.append(origin[j])
        ans="".join(re)
        print(ans)
        origin=re
    else:
        ans="".join(origin)
        str=arr[1]
        ant=ans.replace(str,'1')
        pos=-1
        for j in range(0,len(ant)):
            if ant[j]=='1':
                pos=j
                break
        print(pos)
        