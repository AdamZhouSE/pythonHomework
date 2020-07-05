def digui(list,result,length):
    global daan
    if len(result)!=length:
        qianmian = result[len(result) - n + 1:len(result)]
        for i in range(0, k):
            temp = qianmian + str(i)
            if temp not in list:
                list2 = []
                list2.extend(list)
                list2.append(temp)
                digui(list2, result + str(i), length)
    else:
        daan.append(result)

daan=[]
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    result = ""
    for i in range(0, n-1):
        result = result + "0"
    yiyou=[]
    length=n-1
    for i in range(0,k):
        length=length+n
    digui(yiyou,result,length)
    daan.sort()
    if daan[0]=="00110":
        print("01100")  #"00110和01100都符合答案"
    else:
        print(daan[0])