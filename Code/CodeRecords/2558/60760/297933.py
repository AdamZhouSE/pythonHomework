def func(arr:list):
    length=len(arr)
    if length%2==1:
        return -1
    stack=[]
    for i in arr:
        if i=='}' and len(stack)>0 and stack[-1]=='{':
            stack.pop()
        else:
            stack.append(i)
    res=0
    for i in range(int(len(stack)/2)):
        if stack[i]!='{':
            res+=1
        if stack[-1-i]!='}':
            res+=1
    return res
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(list(input()))
for i in lists:
    print(func(i))