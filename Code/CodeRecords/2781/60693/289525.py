def isPrefix(s1,s2):
    # len(s1)<=len(s2)
    s1Len=len(s1)
    if s1==s2[:s1Len]:
        return True
    return False

def isDecodable(arr:[str]):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if isPrefix(arr[i],arr[j]):
                return True
    return False

t=1
try:
    while True:
        inp=input()
        arr=[]
        while inp!='9':
            arr.append(inp)
            inp=input()
        arr=sorted(arr,key=lambda x:len(x))
        if isDecodable(arr):
            print('Set '+str(t)+' is not immediately decodable')
        else:
            print('Set '+str(t)+' is immediately decodable')
        t+=1
except EOFError:
    pass