n=int(input())
res="YES"
firstLine=input()
x=firstLine[0]
o=firstLine[1]
line=0
while(line<n):
    if(line!=0):
        lineN=input()
    else:
        lineN=firstLine
    for i in range(n):
        if(i==line or i==n-line-1):
            if(lineN[i]!=x):
                res="NO"
                break
        else:
            if(lineN[i]!=o):
                res="NO"
                break
    line+=1
print(res)      