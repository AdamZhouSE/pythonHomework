def numop8():
    num=int(input())
    lst=[]
    for i in range(0,num):
        lst.append(input())
    k=cal_k(lst[0],lst[1])
    res=True
    for i in range(2,len(lst)):
        if cal_k(lst[0],lst[i])==k:
            res=False
            break
    print(res)
    return


def cal_k(str1,str2):
    lst1 = str1.split(',')
    lst2 = str2.split(',')
    k=(float(lst2[1])-float(lst1[1]))/(float(lst2[0])-float(lst1[0]))
    return k

numop8()