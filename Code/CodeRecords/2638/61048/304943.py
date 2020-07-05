import math
def tree7():
    line1=input().split(' ')
    lenth,orderno=int(line1[0]),int(line1[1])
    arr=[int(x) for x in input().split(' ')]
    for i in range(orderno):
        order=input()
        str=[int(x) for x in order.split(' ')]
        if(str[0]==1):
            for i in range(str[1]-1,str[2]):
                arr[i]+=str[3]
        elif str[0]==2 :
            avg=sum(k for k in arr[str[1] - 1:str[2]]) / (str[2] - str[1]+1)
            print('%.4f'%(avg))
        elif str[0]==3:
            avg = sum(k for k in arr[str[1] - 1:str[2]]) / (str[2] - str[1] + 1)
            s=sum(math.pow(k-avg,2) for k in arr[str[1] - 1:str[2]]) / (str[2] - str[1]+1)
            print('%.4f'%(s))


    return

tree7()