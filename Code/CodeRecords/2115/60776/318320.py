lujin=[]
isright=0
count=1
def digui(yizou):
    global isright
    global count
    if(isright==0):
        for i in range(0,len(lujin)):
            if lujin[i][0]==yizou[len(yizou)-1] :
                if lujin[i][1] not in yizou:
                    temp1=[]
                    temp1.extend(yizou)
                    temp1.append(lujin[i][1])
                    digui(temp1)
                else:
                    for j in range(0,len(yizou)):
                        if yizou[j]==lujin[i][1]:
                            if (len(yizou)-j)%2==1:
                                isright=1
                                break
                            else:
                                if len(yizou)-j>2:
                                    count += 1
                                    if count == 2:
                                        isright = 1
                                        break
            if lujin[i][1]==yizou[len(yizou)-1]:
                if lujin[i][0] not in yizou:
                    temp1 = []
                    temp1.extend(yizou)
                    temp1.append(lujin[i][0])
                    digui(temp1)
                else:
                    for j in range(0, len(yizou)):
                        if yizou[j] == lujin[i][0]:
                            if (len(yizou) - j) % 2 == 1:
                                isright = 1
                                break
                            else:
                                if len(yizou)-j>2:
                                    count += 1
                                    if count == 2:
                                        isright = 1
                                        break
a=int(input())
for k in range(0,a):
    a=input().split(' ')
    lujinshu=int(a[1])
    for i in range(0,lujinshu):
        b=input().split(' ')
        for j in range(0,len(b)):
            b[j]=int(b[j])
        lujin.append(b)
    digui([1])
    if isright==1:
        print("NO")
    else:
        print("YES")
    isright=0
    count=0
    lujin.clear()