num=int(input())
def cal(a,b):
    stra=list(bin(a))[2:]
    strb=list(bin(b))[2:]
    stra.reverse()
    strb.reverse()
    length=max(len(strb),len(stra))
    if len(stra)>len(strb):
        for i in range(len(stra)-len(strb)):
            strb.append('0')
    elif  len(stra)<len(strb):
        for i in range(len(strb)-len(stra)):
            stra.append('0')
    for i in range(length):
        if stra[i]!=strb[i]:
            return i+1
    return -1
for i in range(num):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print(cal(arr[0],arr[1]))
