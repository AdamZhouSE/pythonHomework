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
List1=list(map(str,input().split(' ')))
List2=list(map(int,input().split(' ')))
List3=list(map(str,input().split(' ')))
List4=list(map(str,input().split(' ')))
result1=tailInsert(origin,List1[1])
result2=get(result1,List2[1],List2[2])
result3=Insert(result2,int(List3[1]),List3[2])
result4=lookUp(result3,List4[1])
print(result1)
print(result2)
print(result3)
print(result4)