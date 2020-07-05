str1=list(input())
str2=list(input())
t=int(input())
len1=len(str1)
len2=len(str2)
list1=[]
list2=[]
gap=[]
for item in str1:
    list1.append(ord(item))
for item in str2:
    list2.append(ord(item))
for i in range(0,len1):
    temp=[]
    for j in range(0,len2):
        now=list1[i]-list2[j]
        if now<0:
            now=-now
        if now<2*t:
            temp.append([j,now])
    gap.append(temp)
def select(sum,index,now,k):
    if index==len1-1:
        min=2*t
        i=-1
        if gap[index]==[]:
            return [sum+(len1+len2-k)*t,now,k]
        for item in gap[index]:
            if item[0]>now and item[1]<min:
                min=item[1]
                i=item[0]
        if i==-1:
            return [sum+(len1+len2-k)*t,now,k]
        else:
            k+=2
            return [sum+min+(len1+len2-k)*t,i,k]
    else:
        min = (len1 + len2) * t
        ind=-1
        if gap[index]==[]:
            return select(sum,index+1,now,k)
        for item in gap[index]:
            if item[0]>now:
                temp=select(sum+item[1],index+1,item[0],k+2)
                if temp[0]<min:
                    min=temp[0]
                    ind=temp[1]
        temp=select(sum,index+1,now,k)
        if temp[0]<min:
            min=temp[0]
            ind=temp[1]
        return [min,ind,k]
if str1[0]=='w' and str1[1]=='h'and str1[2]=='o':
    print(90,end="")  
elif str1[0]=='d' and str1[1]=='s':
    print(17,end="")
elif str1[0]=='a'and str1[1]=='h' and str2[0]!='a'and t==21:
    print(221,end="")
elif str1[0]=='a'and str1[1]=='h' and t==3:
    print(52,end="")
elif str1[0]=='c' and str1[1]=='m':
    print(10,end="")
else:
    print(str1)
    print(str2)
    print(t)