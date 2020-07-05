time=int(input())
while(time>0):
    time-=1
    length=int(input())
    strr=input()
    listt=strr.split()
    numl=[]
    for n in listt:
        numl.append(int(n))
    for i in numl:
        if(i%2==0):
            print(i,end=' ')
    for i in numl:
        if(i%2!=0):
            print(i,end=' ')
    print()