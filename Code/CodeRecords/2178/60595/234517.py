def Test():
    number=int(input())
    secondline=input().split()
    magic=[]
    for i in range(0,number):
        magic.append(int(secondline[i]))
        print(Func(magic))


def Func(list):
    save=[]
    for i in range(1,len(list)+1):
        for j in range(0,len(list)):
            cell=str(list[j])
            for k in range(j,j+i):
                if(j+i>len(list)):
                    break
                if(j!=k):
                    cell=cell+str(list[k])
            if(i==1 or len(cell)!=1):
                save.append(cell)
    save=set(save)
    return len(save)


if __name__ == "__main__":
    Test()#oh my god 总算是我这个作业里第一个非面向oj纯自测的代码了