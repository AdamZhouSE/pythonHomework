def isvalid(get):
    left=0
    right=0
    for i in get:
        if i=='(':
            left+=1
        elif i==")":
            right+=1
        if(right>left):
            return False
    if(left!=right):
        return False
    return True

get=input()
out=[""]

def deep(current):
    if len(current)<len(out[-1]):
        return
    if isvalid(current) and current not in out:
        out.append(current)
        return
    for i in range(0,len(current)):
        temp=current[0:i]+current[i+1:]
        deep(temp)
deep(get)
max_=len(out[-1])
result=[]
for i in out:
    if len(i)>=max_:
        result.append(i) 
result.sort(reverse=True)
print(result)