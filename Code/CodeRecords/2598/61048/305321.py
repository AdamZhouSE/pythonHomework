def tree9():
    line1=input().split(' ')
    M,D=int(line1[0]),int(line1[1])
    Q=[0]
    arr=[]
    for i in range(M):
        order=input().split(' ')
        if(order[0]=='A'):
            arr.append((Q[-1]+int(order[1]))%D)
        else:
            tmp=arr[len(arr)-int(order[1]):]
            tmp.sort()
            print(tmp[-1])
            Q.append(tmp[-1])

    return

tree9()