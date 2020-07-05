N=int(input())
for n in range(0,N):
    s=input()
    list=[]
    k=-1
    for item in s:
        if item.isalpha():
            print(item,end="")
        else:
            if item=='(':
                temp='0'+'('
                list.append(temp)
                k=k+1
            elif item==')':
                for i in range(k,-1,-1):
                    if(list[k]=='0('):
                        list.pop(i)
                        k=k-1
                        break
                    else:
                        print(list[i][1],end="")
                        list.pop(i)
                        k=k-1
            else:
                if item=='+' or item=='-':
                    temp='1'+item
                elif item=='*' or item=='/':
                    temp='2'+item
                else:temp='3'+item
                if k==-1:
                    list.append(temp)
                    k=k+1
                else:
                    for i in range(k, -1, -1):
                        if (int(temp[0]) <= int(list[i][0])):
                            print(list[i][1], end="")
                            list.pop(i)
                            k = k - 1
                        else:
                            break
                    list.append(temp)
                    k=k+1
    print(list[0][1],end="")
    print("")