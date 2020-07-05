str=input()
a=(len(str)-1)
str=str[1:a]
list=list(map(int,str.split(",")))
list.sort()
c=len(list)-1
b=c-1
a=c-2
max=0
while c>=2:
    while b>=1:
        while a>=0:
            if list[a]+list[b]>list[c]:
                if list[a]+list[b]+list[c]>max:
                    max=list[a]+list[b]+list[c]
            a-=1
        b=-1
        a=b-1
    c-=1
    b=c-1
    a=c-2
print(max)
