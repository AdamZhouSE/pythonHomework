def hassame(a,b):
    if len(a)<len(b):
        for i in range(len(a)):
            if a[i] in b:
                return True
    if len(a)>=len(b):
        for i in range(len(b)):
            if b[i] in a:
                return True
    return False

out=[0]
def deep(index,temp,get):
    out[0]=max(out[0],len(temp))
    for i in range(index,len(get)):
        if not hassame(temp,get[i]):
            deep(i+1,temp+get[i],get) 
get=eval(input())
deep(0,"",get)
print(out[0])