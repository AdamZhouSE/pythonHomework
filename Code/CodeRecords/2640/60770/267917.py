def solve():
    src=input()
    des=list(input())

    def hasAll(s1='',li=[]):
        for l in li:
            if s1.count(l)==0:
                return False
        return True

    res=src
    for i in range(len(src)-2):
        for j in range(i+1,len(src)):
            cur=src[i:j+1]
            if hasAll(cur,des):
                if j-i<len(res):
                   res=cur

    print(res)
if  __name__ == '__main__' :
    solve()