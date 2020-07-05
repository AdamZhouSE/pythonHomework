n=int(input())
str1=input()
len1=len(str1)
str1=str1[1:len1-1]
str1=str1.split(',')
str1=list(map(int,str1))
len1=len(str1)
str2=input()
len2=len(str2)
str2=str2[1:len2-1]
str2=str2.split(',')
str2=list(map(int,str2))
i=len1-1
while(i>0):
    j=i-1
    while(j>=0):
        if(str1[i]>str1[j]):
            temp1=str1[j]
            str1[j]=str1[i]
            str1[i]=temp1
            temp2 = str2[j]
            str2[j] = str2[i]
            str2[i] = temp2
        j-=1
    i-=1
list=[]
i=0
while(i<len1):
    t=(n-str1[i])/str2[i]
    list.append(t)
    i+=1
i=0
count=1
while(i<len1-1):
    if(list[i]<list[i+1]):
        count+=1
    i+=1
print(count)