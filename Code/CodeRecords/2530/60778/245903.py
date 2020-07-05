str_a=input()
str_b=list(input())
for i in range(1,len(str_b)):
    tmp=i-1
    while(tmp>=0 and str_a.find(str_b[tmp])>str_a.find(str_b[tmp+1])):
        x=str_b[tmp]
        str_b[tmp]=str_b[tmp+1]
        str_b[tmp+1]=x
        tmp-=1
print(str_b)