a=int(input())
i=1
while a>len(str(i+1)):
    a-=len(str(i))
    i+=1
list=list(map(int,str(i)))
print(list[a-1])