a = int(input())
for i in range(a):
    b = list(input())
    sum = 0
    numOf0,numOf1,numOf2 = 0 , 0, 0 
    for k in range(b.__len__()-1):
        for j in range(k+2,b.__len__()):
            s = b[k:j+1]
            for m in s:
                if m == '0':
                    numOf0 += 1
                if m == '1':
                    numOf1 += 1
                if m == '2':
                    numOf2 += 1
            if (numOf1 == numOf2) and (numOf1== numOf0):
                sum += 1
            numOf0,numOf1,numOf2 = 0 , 0, 0     
    print(sum)            
                             