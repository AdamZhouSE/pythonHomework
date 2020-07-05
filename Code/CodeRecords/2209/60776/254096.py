import sys

sys.setrecursionlimit(300002)
def jianfa(str,list,int):
    if len(str)<=int+1:
        return 0
    else:
        count=-1
        weizhi=-1
        for i in range(0,len(list)):
            for j in range(0,len(list[i])):
                if int+2+j-len(list[i])>=0&int+2+j<len(str):
                    if str[int+2+j-len(list[i]):int+2+j]==list[i]:
                        if j+1>count:
                            count=j+1
                            weizhi=i
        if count<0:
            return -9999
        else:
            return jianfa(str,list,int+count)+1

if __name__ == "__main__":
    shuliang = int(input())
    zongwen = input()
    danci = []
    for i in range(0, shuliang):
        a = input();
        if a in zongwen:
            danci.append(a)
    b=jianfa(zongwen,danci,-1)
    if b<0:
        print(-1)
    else:print(b)



