string=input()

maxLetter=int(input())
minSize=int(input())
maxSize=int(input())
countMax=0
for i in range(minSize,maxSize+1):
    j=0
    while j+i<len(string):
        if len(set(string[j:j+i]))<=maxLetter:
            y=string[j:j+i]
            count=1
            k=j+1
            while k+i<=len(string):
                if y==string[k:k+i]:
                    count=count+1
                k=k+1
            countMax=max(countMax,count)
        j=j+1
print(countMax)