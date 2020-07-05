n = int(input())
result = []
for i in range(1,int(n/2)+1):
    has_zero = False
    a = str(i)
    b = str(n-i)
    for j in range(0,len(a)):
        if j<len(a):
            if a[j:j+1]=="0":
                has_zero = True
                break
    if has_zero ==False:
        for j in range(0,len(b)):
            if j<len(b):
                if b[j:j+1] =="0":
                    has_zero = True
                    break
        if has_zero ==False:
            result.append(int(a))
            result.append(int(b))
            print(result)
            break