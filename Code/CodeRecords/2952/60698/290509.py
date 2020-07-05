def test():
    operations=input()
    n=int(input())
    stack=[]
    strs=[]
    for i in range(0,len(operations)):
        if operations[i]=='B':
            stack.pop()
        elif operations[i]=='P':
            strs.append(''.join(stack))
        else:
            stack.append(operations[i])
    for _ in range(0,n):
        xy=input().split()
        x=int(xy[0])
        y=int(xy[1])
        x=strs[x-1]
        y=strs[y-1]
        print(y.count(x))

test()