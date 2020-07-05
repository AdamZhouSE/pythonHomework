def tailInsert(origin,string):
    return origin+string

def get(origin,a,b):
    return origin[a:a+b]

def Insert(origin,place,newstring):
    start=origin[0:place]
    string=origin.replace(start,'',1)
    return start+newstring+string

def lookUp(origin,string):
    for start in range(len(origin)-len(string)+1):
        if origin[start:start+len(string)]==string:
            return start
    return -1

a=int(input())
origin=input()
List=[]
for i in range(a):
    List.append(list(map(str,input().split(' '))))    
for i in range(a):
    if List[i][0]=='1':
        origin=tailInsert(origin,str(List[i][1]))
        print(origin)
    elif List[i][0]=='2':
        origin=get(origin,int(List[i][1]),int(List[i][2]))
        print(origin)
    elif List[i][0]=='3':
        origin=Insert(origin,int(List[i][1]),List[i][2])
        print(origin)
    else:
        print(lookUp(origin,List[i][1]))
    