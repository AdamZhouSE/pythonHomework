def insert(version,x):
    version.append(x)
    return version
def delete(version,x):
    if(x in version):
        version.remove(x)
    return version
def query(version,x):
    return(version.index(x)+1)
def query2(version,n):
    version.sort()
    return version[n-1]
def prex(version,x):
    version.sort()
    for i in range(1,len(version)):
        if(version[i-1]<x and version[i]>=x):
            return version[i-1]
    if(x<=version[0]):
        return int(-2**31+1)
    else:
        return max(version)
def nextx(version,x):
    version.sort()
    for i in range(1,len(version)):
        if(version[i-1]<=x and version[i]>x):
            return version[i]
    if(x>=version[-1]):
        return int(2**31)
    else:
        return min(version)
t=int(input())
versions=[[] for i in range(t)]
for i in range(t):
    vID,opt,x=map(int,input().split())
    #print(vID,opt,x)
    if(opt==1):
        versions[i+1]=(insert(versions[vID][:],x))
    elif(opt==2):
        versions[i+1]=(delete(versions[vID][:],x))
    elif(opt==3):
        print(query(versions[vID],x))
        versions[i+1]=versions[vID][:]
    elif(opt==4):
        print(query2(versions[vID],x))
        versions[i+1]=versions[vID][:]
    elif(opt==5):
        print(prex(versions[vID],x))
        versions[i+1]=versions[vID][:]
    else:
        print(nextx(versions[vID],x))
        versions[i+1]=versions[vID][:]
    