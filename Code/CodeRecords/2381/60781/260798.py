num1=input()
len1=(len(num1)+1)/2
num2=input()
len2=(len(num2)+1)/2
i=0
res1=0
while i<len1:
    if(num1[i*2]=='1'):
        res1+=(-2)**(len1-i-1)
    else:
        res1+=0
    i+=1
i=0
res2=0
while i<len2:
    if(num2[i*2]=='1'):
        res2+=(-2)**(len2-i-1)
    else:
        res2+=0
    i+=1
r=res1+res2

if(r==0):
    print('0')
else:
    res=""
    while (r != 0) :
        if(r%2==0):
            res="0"+res
            r=int(r/(-2))
        else:
            res="1"+res
            r=int((r-1)/(-2))
    res=list(res)
    res=list(map(int,res))
    print(res)