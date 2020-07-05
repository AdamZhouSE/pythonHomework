if __name__=="__main__":
    m=int(input())
    n=int(input())
    op_num=int(input())
    ops=[]
    matrix=[[0]*n for _ in range(m)]
    if op_num:
        for i in range(op_num):
            ops.append(input().split(","))
    for op in ops:
        m = min(m,int(op[0]))
        n =min(n,int(op[1]))
    print(m*n)