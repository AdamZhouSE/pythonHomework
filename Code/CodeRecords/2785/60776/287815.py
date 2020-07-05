is0="NO"
def difui(x,list,zongzhi):
    global is0
    if(x==len(list)-1):
        if(zongzhi+list[x]==0 or zongzhi-list[x]==0 or zongzhi-list[x]==360 or zongzhi+list[x]==360):
            is0="YES"
    else:
        difui(x+1,list,zongzhi+list[x])
        difui(x+1,list,zongzhi-list[x])




if __name__ == "__main__":
    a=int(input())
    zong=[]
    for i in range(0,a):
        zong.append(int(input()))
    difui(0,zong,0)
    print(is0)