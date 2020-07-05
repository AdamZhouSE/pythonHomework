# https://zhuanlan.zhihu.com/p/37495930

def solve():
    start=list(input())
    end=list(input())

    le1,le2=len(start),len(end)
    if le1!=le2:
        print("False")
        return

    i,j=0,0
    while True:
        if i != le1:
            while(start[i]=='X'):
                i+=1
                if i==le1:
                    break
        if j!=le2:
            while(start[j]=='X'):
                j+=1
                if j==le2:
                    break
        if (i==le1 or j==le2):
            if not (i==le1 and j==le2):
                print("False")
                return
            print("True")
            return

        if start[i]!=end[j]:
            print("False")
            return

        if start[i]=='L' and i<j:
            print('False')
            return
        if start[i]=='R' and i>j:
            print('False')
            return
        i+=1
        j+=1

if  __name__ == '__main__' :
    solve()
