import functools
def postfix_sort():
    str=input()
    res=[]
    for i in range(0,len(str)):
        res.append(str[i:])
    temp=sorted(res,key=functools.cmp_to_key(cmp))
    loc=[]
    for postfix in temp:
        loc.append(res.index(postfix)+1)
    for num in loc:
        print(num,end=" ")

def cmp(a,b):
    if a[0]<b[0]:
        return -1
    elif a[0]>b[0]:
        return 1
    else:
        if len(a)<len(b):
            return -1
        else:
            return 1

if __name__=='__main__':
    postfix_sort()