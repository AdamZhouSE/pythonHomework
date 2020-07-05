def judge(x1,y1,x2,y2,x3,y3,x4,y4):
    #未通过快速排斥，不相交
    if not min(y1,y2)<max(y3,y4) and min(y3,y4)<max(y1,y2) and min(x1,x2)<max(x3,x4) and min(x3,x4)<max(x1,x2):
        return 0
    #通过快速排斥未通过跨立实验，不相交 类似于（a,b)(c,d)两个向量 计算两个ad-bc
    fc=(y4-y1)*(x2-x1)-(x4-x1)*(y2-y1)
    fb=(y3-y1)*(x2-x1)-(x3-x1)*(y2-y1)
    if fc*fb>0:
        return 0
    return 1


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        x1,y1,x2,y2=input().split()
        x3,y3,x4,y4=input().split()
        res=judge(int(x1),int(y1),int(x2),int(y2),int(x3),int(y3),int(x4),int(y4))
        #print("{} {} {} {} {} {} {} {}".format(x1, y1, x2, y2, x3, y3, x4, y4))
        print(res)