def f(string):
    slist=''
    for i in range(len(string)):
        slist+=str(string[-i-1])
    print(slist,end='')
string=str(input())
f(string)