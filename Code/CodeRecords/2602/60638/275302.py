numbersA=list(map(int,input()[1:-1].split(",")))
numbersB=list(map(int,input()[1:-1].split(",")))
maxlength=0
for i in range(0,len(numbersA)):
    for j in range(0,len(numbersB)):
        if numbersA[i]==numbersB[j]:
            length=0
            k=i
            m=j
            while i<len(numbersA)and j<len(numbersB) and numbersA[i]==numbersB[j]:
                i=i+1
                j=j+1
                length=length+1
            maxlength=max(maxlength,length)
            i=k
            j=m
print(maxlength)