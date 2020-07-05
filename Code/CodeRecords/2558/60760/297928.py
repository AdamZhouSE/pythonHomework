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
    res=len(stack)
    if len(stack)>0:
        res=len(stack)-1
    return res
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(list(input()))
for i in lists:
    print(func(i))