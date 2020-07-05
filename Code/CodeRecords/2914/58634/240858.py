t = int(input())
for i in range(t):
    n = int(input())
    result = True
    array1 = [int(i) for i in input().split(" ")]
    array2 = [int(i) for i in input().split(" ")]
    k = 0
    over = False
    for j in range(n):
        if(array1[j]!=array2[j]):
            if(over):
                result = False
                break
            if k == 0:#初始化k
                k = array1[j]-array2[j]
                if(k>0):
                    result = False
                    break
                continue
        if(k!=0):
            if(array1[j]-array2[j]!=k and array1[j]-array2[j]!=0):
                result = False
                break
            if(array1[j]-array2[j]==0):
                over = True
    if(result):
        print("YES")
    else:
        print("NO")

