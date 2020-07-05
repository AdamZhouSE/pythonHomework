def getSubset(str):
    if str is None or len(str) < 1:
        return ""
    arr = []
    arr.append(str[0])
    i = 1
    while i < len(str):
        lens = len(arr)
        j = 0
        while j < lens:
            arr.append(arr[j] + str[i])
            j += 1
        arr.append(str[i])
        i += 1
    return arr
def panduan(str):
    final=True
    for index in range(len(str)):
        if str[index]=='b':
            for index1 in range(index+1,len(str)):
                if str[index1]=='a':
                    final=False
                    break
        if str[index]=='c':
            for index1 in range(index+1,len(str)):
                if str[index1]=='a' or str[index1]=='b':
                    final=False
                    break
    return final
n=int(input())
for i in range(n):
    s=input()
    zc=[]
    res=0
    for index in range(len(s)):
        if s[index]=='a':
            zc.append(index)
    for zcs in zc:
        oc=getSubset(s[zcs+1:])
        for ocs in oc:
            if ocs[0]!='c' and ocs[len(ocs)-1]=='c' and 'b' in ocs and panduan(ocs):
                res+=1
    print(res)

