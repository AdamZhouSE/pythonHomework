lines=int(input())
goin=[]
for i in range(lines):
    goin.append(input().split(" "))
for i in range(lines):
    lists=[]
    str1=str(goin[i][0])
    number=int(goin[i][1])
    for j in range(1,len(str1)+1):
       for n in range(len(str1)-j+1):
           temp=str1[n:n+j]             #str中长度为i得子串
           count=0
           for m in range(len(str1)-j+1):
               if str1[m:m+j]==temp:
                   count=count+1
           if count==number:
                lists.append(temp)
    lists=set(lists)   #去掉重复得子串
    lengths=[]         #把子串转化为长度
    for i in lists:
        lengths.append(len(i))
    temp2=set(lengths)
    result=-1
    final=-1
   # print(temp2)
    for x in temp2:
        if lengths.count(x)>=result:
            result= lengths.count(x)
            final=x
   # print(lists)
   # print(lengths,lengths.count(1))
    print(final)
