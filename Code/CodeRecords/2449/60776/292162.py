def chazhao(list,qi,zhong,target):
    if qi==zhong:
        if list[qi]==target:
            print(qi)
        else:
            print(-1)
    else:
        zhongjian=int((qi+zhong)/2)
        if list[qi]>target and list[zhong]>=target:
            chazhao(list,zhongjian,zhong,target)
        else:
            chazhao(list,qi,zhongjian,target)




if __name__ == "__main__":
    b = input().split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    target = int(input())
    chazhao(b,0,len(b)-1,target)
