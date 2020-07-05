case_num=0
node=input()
while node!='-1':
    case_num=case_num+1
    temp=node
    while temp[len(temp)-5:]!='-1 -1':
        temp=input()
        node=node+' '+temp
    array=node.split()
    current=int(array[0])
    count=0
    flag=True
    stack=[[count,current,flag]]
    visited=[]
    for i in range(1,len(array)):
        if array[i]!='-1':
            current=int(array[i])
            if flag:
                count=count-1
                stack.append([count,current,flag])
            else:
                count=count+1
                stack.append([count,current,flag])
                flag=not flag
        else:
            if flag:
                flag=not flag#切换为左或右子树
            else:
                before=stack.pop()
                while not before[2]:
                    visited.append(before)
                    if len(stack)==0:
                        break
                    before=stack.pop()
                visited.append(before)
                count=before[0]+1
            stack.append([0,0,flag])
    visited.sort()
    summary=0
    list=[]
    result=[]
    for item in visited:
        if list.count(item[0])==0:
            if summary!=0:
                result.append(str(summary))
            list.append(item[0])
            summary=item[1]
        else:
            summary=summary+item[1]
    result.append(str(summary))
    print("Case "+str(case_num)+":\n"+' '.join(result),end='\n\n')
    node=input()