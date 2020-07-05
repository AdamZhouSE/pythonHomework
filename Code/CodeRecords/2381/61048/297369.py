import math
def numop24():
    string1=input().split(',')
    arr1=[int(x) for x in string1]
    string2 = input().split(',')
    arr2 = [int(x) for x in string2]
    addition=bin_to_inte((arr1))+bin_to_inte(arr2)
    res=[int(x) for x in str(numop21(addition))]

    print(res)
    return 0



def bin_to_inte(a):
    res=0
    for i in range(len(a)):
        res+=math.pow(-2,(len(a)-1-i))*int(a[i])
    return res


def numop21(num):

    res=''
    while(num!=1 and num!=0):
        res=str(abs(int(num%(-2))))+res
        if(num>0):
            num=int(num/-2)
        else:
            if(num%-2!=0):
                num=int((num/-2)+1)
            else:
                num=int(num/-2)
    if(num==1):
        res='1'+res

    return res


numop24()