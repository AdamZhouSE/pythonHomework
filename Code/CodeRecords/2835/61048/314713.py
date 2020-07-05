def arr15():
    n=int(input())
    cards=[int(x) for x in input().split(" ")]
    cnt_5=0
    cnt_0=0
    res=0
    for num in cards:
        if num==5:
            cnt_5+=1
        elif num==0:
            cnt_0+=1
    if(cnt_0<1):print("-1")
    elif(cnt_0>=1 and cnt_5<9):
        print("0")        
    else:
        cnt_5=(cnt_5//9)*9
        res=''
        for i in range(cnt_5):
            res+="5"
        for i in range(cnt_0):
            res+="0"
        print(res)
    return
arr15()