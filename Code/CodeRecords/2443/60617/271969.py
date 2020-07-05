import functools

def compare(a, b):
    res1=a+b
    res2=b+a
    if res1>res2:
        return 1
    elif res1==res2:
        return 0
    else:
        return -1

def max_Num():
    arr=list(map(str,eval(input())))
    arr=sorted(arr, key=functools.cmp_to_key(compare))
    arr.sort()
    res=""
    for ele in arr[::-1]:
        res+=ele
    print(res)
   



if __name__=='__main__':
    max_Num()
