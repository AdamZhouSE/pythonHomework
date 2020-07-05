def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]
tests=(int)(input())
for i in range(0,tests):
    for i in range(0,3):
        a=input().split(' ')
        b=input().split(' ')
        c=input().split(' ')
        range_min=[]
        range_max=[]
        range_min.append(min((int)(a[0]),(int)(c[0]),(int)(b[0])))
        range_min.append(min((int)(a[1]),(int)(c[1]),(int)(b[1])))
        range_max.append(max((int)(a[0]),(int)(c[0]),(int)(b[0])))
        range_max.append(max((int)(a[1]),(int)(c[1]),(int)(b[1])))
        dots=0
        for i in range(range_min[0]+1,range_max[0]):
            for j in range(range_min[1]+1,range_max[1]):
                p=[i,j]
                pa = [i - (int)(a[0]), j - (int)(a[1])]
                pb = [i - (int)(b[0]), j - (int)(b[1])]
                pc = [i - (int)(c[0]), j - (int)(c[1])]
                t1=cross(pa,pb)
                t2=cross(pb,pc)
                t3=cross(pc,pa)
                if(t1*t2 > 0 and t1*t3 > 0):
                    dots+=1
        print(dots)