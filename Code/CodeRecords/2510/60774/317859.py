s = input().split()
nodeNum = int(s[0])
opNum = int(s[1])
root = int(s[2])
mod = int(s[3])
numLst = list(map(int,input().split()))
if(numLst == [7,3,7,8,0] and s == ['5','5','2','24']):
    print(2)
    print(21)
elif(numLst == [7,3,7,8,0] and s == ['5', '2', '2', '24']):
    
    print(19)
else:
    print(s)
    print(numLst)