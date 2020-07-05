str1 = str(input())
lis = str1[1:len(str1)-1].split(",")
lis = [int(x) for x in lis]
lis.sort()
if(len(lis)<2):
    print ("0")
else:
    res = []
    for i in range(len(lis)-1):
        res.append(lis[i+1] - lis[i])
    print (max(res))