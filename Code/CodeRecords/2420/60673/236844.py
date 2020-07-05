n = int(input())
res = []
for i in range(1,n):
    log = True
    res2 = n - i
    str1 = str(i)
    str2 = str(res2)
    for j in range(len(str2)):
        if(str2[j:j+1]=="0"):
            log = False
    for j in range(len(str1)):
        if(str1[j:j+1]=="0"):
            log = False
    if(log==True):
        res = [i,res2]
        break
print (res)