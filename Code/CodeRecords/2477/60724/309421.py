def line(a,b,c,d,e,f):
    return c<a<e and f<b<e

T=int(input())
for m in range(T):
    string1=input().split(" ")
    string2=input().split(" ")
    x1,y1,x2,y2=int(string1[0]),int(string1[1]),int(string1[2]),int(string1[3])
    x3,y3,x4,y4=int(string2[0]),int(string2[1]),int(string2[2]),int(string2[3])
    if line(x1,y1,x3,y3,x4,y4) or line(x2,y2,x3,y3,x4,y4) or line(x3,y3,x1,y1,x2,y2) or line(x4,y4,x1,y1,x2,y2):
        print(1)
    else:
        print(0)