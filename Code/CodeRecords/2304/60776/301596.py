list=[]
chengshu=1
isfanzhuan=0
def digui1(dangqian):
    global list
    global chengshu
    print("Level ",end="")
    print(chengshu,end="")
    print(" : ",end="")
    print(" ".join(str(i) for i in dangqian))
    xiayihang=[]
    for i in range(0,len(dangqian)):
        for j in range(0,len(list)):
            if list[j][0]==dangqian[i]:
                if list[j][1] != 0:
                    xiayihang.append(list[j][1])
                if list[j][2] != 0:
                    xiayihang.append(list[j][2])
    if xiayihang!=[]:
        chengshu=chengshu+1
        digui1(xiayihang)
def digui2(dangqian):
    global list
    global chengshu
    global isfanzhuan
    print("Level ",end="")
    print(chengshu,end="")
    if isfanzhuan==0:
        isfanzhuan=1
        print(" from left to right: ",end="")
        print(" ".join(str(i) for i in dangqian))
    else:
        isfanzhuan=0
        print(" from right to left: ",end="")
        dangqian.reverse()
        print(" ".join(str(i) for i in dangqian))
        dangqian.reverse()
    xiayihang=[]
    for i in range(0, len(dangqian)):
        for j in range(0, len(list)):
            if list[j][0] == dangqian[i]:
                if list[j][1] != 0:
                    xiayihang.append(list[j][1])
                if list[j][2] != 0:
                    xiayihang.append(list[j][2])
    if xiayihang!=[]:
        chengshu=chengshu+1
        digui2(xiayihang)

if __name__ == "__main__":
    a=input().split(' ')
    root=int(a[1])
    hangshu=int(a[0])
    for i in range(0,hangshu):
        b=input().split(' ')
        for j in range(0,len(b)):
            b[j]=int(b[j])
        list.append(b)
    digui1([root])
    chengshu=1
    digui2([root])