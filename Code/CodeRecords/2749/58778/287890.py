n=int(input())
numlist=list(map(int,input().split( )))
numlist=[0]+numlist
s=input()
numstr=[]
for i in range(n):
    numstr.append((numlist[i],s[i]))
strlist=[]
for i in range(n):
    temp=''
    j=i
    if(numstr[j][0]==0):
        temp+=numstr[j][1]
    else:
        while numstr[j][0]!=0:
            temp+=numstr[j][1]
            j=numstr[j][0]-1
        temp+=numstr[j][1]
    strlist.append((numstr[i][0],temp,i+1))
def order(tem):
    return tem[1]
strlist.sort(key=order)
for i in range(n-1):
    if(strlist[i][1]==strlist[i+1][1]):
        temp1=strlist[i]
        temp2=strlist[i+1]
        while(temp1[1]==temp2[1] and temp1[0]!=1):
            for r in range(n):
                if(temp1[0]==strlist[r][2]):
                    temp1=strlist[r]
            for r in range(n):
                if (temp2[0] == strlist[r][2]):
                    temp2 = strlist[r]
        if(temp1[1]>temp2[1] and temp1[0]!=1):
            strlist[i],strlist[i+1]=strlist[i+1],strlist[i]
        elif temp1[0]==1:
            if(temp1[2]>temp2[2]):
                strlist[i],strlist[i+1]=strlist[i+1],strlist[i]
for i in range(n):
    print(strlist[i][2],'',end='')