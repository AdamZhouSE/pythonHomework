def evaluate(x,sourse):
    return sourse.find(x)




string=list(input())
sourse=input()
for i in range(1,len(string)):
    tmp=i-1
    while(tmp>=0 and evaluate(string[tmp],sourse)>evaluate(string[tmp+1],sourse)):
        x=string[tmp]
        string[tmp]=string[tmp+1]
        string[tmp+1]=x
        tmp-=1
print("".join(string))