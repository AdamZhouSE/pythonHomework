n=int(input())
s=[]
while n>0:
    str=input()
    n=n-1
    temp=''
    for item in str:
        if item>='0' and item<='9':
            temp=temp+item
        elif item>='A' and item<='Z':
            if item=='A' or item=='B' or item=='C':
                temp=temp+'2'
            elif item=='D' or item=='E' or item=='F':
                temp=temp+'3'
            elif item=='G' or item=='H' or item=='I':
                temp=temp+'4'
            elif item=='J' or item=='K' or item=='L':
                temp=temp+'5'
            elif item=='M' or item=='N' or item=='O':
                temp=temp+'6'
            elif item=='P' or item=='R' or item=='S':
                temp=temp+'7'
            elif item=='T' or item=='U' or item=='V':
                temp=temp+'8'
            else:
                temp=temp+'9'
        else:
            continue
    s.append(temp)
t=0
used=[]
for i in range(0,len(s)-1):
    tel=s[i]
    num=1
    for j in range(i+1,len(s)):
        if s[j]==tel:
            num=num+1
    if num>1:
        
        result=tel[0:3]+'-'+tel[3:7]
        ifused='no'
        for item in used:
            if item==result:
                ifused='yes'
        if ifused=='no':
            t=t+1
            used.append(result)
            print(result,end=' ')
            print(num)
if t==0:
    print('No duplicates.',end='')