a=int(input())
i=1
while a>=len(str(i)):
    a-=len(str(i))
    i+=1
list=list(map(int,str(i+1)))
print(list[a]-1)