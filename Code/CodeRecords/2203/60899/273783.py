str0 = input()
for m in range(1,len(str0)+1):
    str1 = str0[0:m]
    length = len(str1)
    lengthOfprefix = 0
    for i in range(0,length-1):
        for j in range(i+1,length):
            for k in range(1,length-i+1):
                if i>=0 and j<=i+k-1 and j+k-1<=length-1:
                    #print(str(i) + " " + str(j) + " " + str(k))
                    if str1[i:i+k-1+1] == str1[j:j+k-1+1]:
                        lengthOfprefix += k
    print(lengthOfprefix)
