# https://www.jianshu.com/p/f4d7dbcb1db3
def solve():
    row=list(map(int,input()[1:-1].split(',')))
    # res=0
    # dict={x:i for (i,x) in enumerate(row)}
    # n=len(row)
    # for i in range(0,n,2):
    #     x=row[i]
    #     if x%2==0:
    #         y=x+1
    #     else:
    #         y=x-1
    #     j=dict[y]
    #     if abs(i-j)>1:
    #         row[i+1],row[j]=row[j],row[i+1]
    #         dict[row[i+1]],dict[row[j]]=i+1,j
    #         res+=1
    # print(res)

    #https://leetcode-cn.com/problems/couples-holding-hands/solution/qing-lu-qian-shou-by-leetcode/
    res = 0
    for i in range(0, len(row), 2):
        x = row[i]
        if row[i + 1] == x ^ 1: continue
        res += 1
        for j in range(i + 1, len(row)):
            if row[j] == x ^ 1:
                row[i + 1], row[j] = row[j], row[i + 1]
                break
    print(res)


if __name__ == '__main__':
    solve()