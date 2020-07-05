def numop13():
    num=int(input())
    points=[]
    max=2
    for i in range(num):
        points.append(input())
    for i in range(num):
        for j in range(i+1,num):
            k=cal_k(points[i],points[j])
            count=2
            for m in range(0,num):
                if(m!=i and m!=j):
                    if(cal_k(points[i],points[m])==k):
                        count+=1
            if(count>max):
                max=count
    print(max)
    return

def cal_k(str1,str2):
    lst1 = str1.split(',')
    lst2 = str2.split(',')
    if(int(lst1[0])-int(lst2[0])==0):
        k=999
    else:
        k=(float(lst2[1])-float(lst1[1]))/(float(lst2[0])-float(lst1[0]))
    return k

numop13()