a=int(input())
for k in range(0,a):
    a=input().split(' ')
    jishu=int(a[1])
    a=input().split(' ')
    c=[]
    for i in range(0,len(a)):
        if int(a[i])%jishu==0:
            c.append(a[i])
    a=c
    if a==[]:
        print(0)
    else:
        for i in range(0, len(a)):
            a[i] = int(a[i])
            a[i] = bin(a[i])
            a[i] = a[i].replace("0b", "")
            for j in range(0, 8 - len(a[i])):
                a[i] = "0" + a[i]
        result = ""
        for i in range(0, len(a[0])):
            isyi = 0
            for j in range(0, len(a)):
                if a[j][i] == '1':
                    result = result + "1"
                    isyi = 1
                    break
            if isyi == 0:
                result = result + "0"
        result = int(result, 2)
        print(result)