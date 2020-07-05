d={}
e={}
a=input()
b=input()
def solution(a,b):
    if(len(a)>len(b)):
        return False
    else:
        start=0
        end=0
        while end<len(a):
            if b[end] in d:
                d[b[end]]=d[b[end]]+1
            else:
                d[b[end]]=1
            if a[end] in e:
                e[a[end]]=e[a[end]]+1
            else:
                e[a[end]]=1
            end+=1
        def mapping(d,e:dict):

            for i in e.keys():
                if(i not in d) or d[i]!=e[i]:
                    return False
            return True
        end-=1
        while end<len(b):
            if(mapping(d,e)):return True

            d[b[start]]-=1
            start+=1

            end+=1
            if(end==len(b)):
                return False
            if b[end] in d:
                d[b[end]]=d[b[end]]+1
            else:
                d[b[end]]=1
print(solution(a,b))


