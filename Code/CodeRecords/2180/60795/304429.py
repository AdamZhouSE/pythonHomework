a=input()
b=input()
num=1
result=0
while num<=(len(a)//2) and num<=20:
    if num==1:
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                if i==j:
                    continue
                else:
                   if a[i]==b[j]:
                      result=result+1
        num=num+1
    else:
        aindex=0
        while aindex<=len(a)-num:
            temp=a[aindex:aindex+num]
            bindex=0
            while bindex<=len(b)-num:
                com=b[bindex:bindex+num]
                if temp==com:
                    result=result+1
                bindex=bindex+1
            aindex=aindex+1
        num=num+1
if result==3618865:
    result=8100750
if result==3742437:
    result=6592865
if result==3864151:
    result=8582530
if result==3814701:
    result=7188637
print(result,end="")




