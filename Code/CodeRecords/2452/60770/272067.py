import bisect

def solve():
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split(','))))
    target=int(input())
    first=list(map(lambda x:x[0],matrix))
    loc=bisect.bisect_left(first,target)-1
    #print(loc)
    line=matrix[loc]
    loc=bisect.bisect_left(line,target)
    #print(loc)
    if line[loc]==target:
        print("True")
    else:
        print('False')

if  __name__ == '__main__' :
    solve()