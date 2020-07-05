def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

class InRect(object):

    def __int__(self):
        self.__isInRectFlag = False

    def cross_product(self, xp, yp, x1, y1, x2, y2):
        return (x2 - x1) * (yp - y1)-(y2 - y1) * (xp - x1)

    def compute_para(self, xp, yp, xa, ya, xb, yb, xc, yc, xd, yd):
        cross_product_ab = InRect().cross_product(xp, yp, xa, ya, xb, yb)
        cross_product_bc = InRect().cross_product(xp, yp, xb, yb, xc, yc)
        cross_product_cd = InRect().cross_product(xp, yp, xc, yc, xd, yd)
        cross_product_da = InRect().cross_product(xp, yp, xd, yd, xa, ya)
        return cross_product_ab,cross_product_bc,cross_product_cd,cross_product_da

    def is_in_rect(self, aa, bb, cc, dd):
        if (aa > 0 and bb > 0 and cc > 0 and dd > 0) or (aa < 0 and bb < 0 and cc < 0 and dd < 0):
            self.__isInRectFlag= True
        else:
            self.__isInRectFlag = False

        return self.__isInRectFlag

nd=nums(input())
n,d=nd[0],nd[1]
m=int(input())
for i in range(m):
    point=nums(input())
    aa,bb,cc,dd=InRect().compute_para(point[0],point[1],0,d,d,0,n,n-d,n-d,n)
    judge=InRect().is_in_rect(aa, bb, cc, dd)
    if judge:
        answer='YES'
        print(answer)
    else:
        answer='NO'
        print(answer)