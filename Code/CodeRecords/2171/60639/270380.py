def operation(list):
    even=[]
    odd=[]
    for i in range(len(list)):
        if list[i]%2==1:
            odd.append(list[i])
        else:
            even.append(list[i])
    targetList=even+odd
    result=''
    for i in range(len(targetList)):
        result+=str(targetList[i])+' '
    return result

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(operation(arr))