#string 15
def test():
    n=int(input())
    origin=input()
    res=''
    for i in range(0,len(origin)):
        ansc=((ord(origin[i])-ord('a')+n)%26)+ord('a')
        c=chr(ansc)
        res=res+c
    print(res,end='')

test()