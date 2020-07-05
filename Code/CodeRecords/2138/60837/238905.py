def isIt(list,num):
    for i in range(2,len(list)+1):
        for j in range(0,len(list)-i+1):
            number=0
            for k in range(j,j+i):
                number+=list[k]
            if number%num==0:
                return True
    return False

list=list(map(int,input().split(',')))
num=int(input())
print(isIt(list,num))