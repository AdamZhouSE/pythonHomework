str=input()
def W(s):
    result=[]
    for i in range(len(s)):
        for j in range(len(s)-i):
            temp=s[j:j+i+1]
            if temp not in result:
                result.append(temp)
    return result
def Y(s):
    result=[]
    for i in range(len(s)):
        result+=divide(s,i,[],'')
    return result

def divide(remaining,key,result,store):
    if key>=0:
        for i in range(len(remaining)-key):
            temp=remaining[i+1:]
            result=divide(temp,key-1,result,store+remaining[i])
        return result
    else:
        if store not in result:
            result.append(store)
        return result

count=0
for i in W(str):
    judge=True
    if W(i)==Y(i):
        count+=1
print(count)