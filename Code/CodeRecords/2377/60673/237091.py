len = int(input())
a = input().split(",")
b = input().split(",")
c = input().split(",")
log = True
if(a[0]==b[0] and a[0]==c[0]):
    log = False
if((int(a[1])-int(b[1]))/(int(a[0])-int(b[0])) == (int(c[1])-int(b[1]))/(int(c[0])-int(b[0]))):
    log = False
print (log)