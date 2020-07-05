def pen( a , b , c , d):
    if c in sum and d in sum:
        return
    if c not in sum:
        sum.append(c)
    if d not in sum:
        sum.append(d)
    if b >= c :
        pen(a,b,c,b-c)
    if a >= d:
        pen(a,b,a-d,d)
a = int(input())
b = int(input())
c = int(input())
sum = []
pen(a , b, 0 , 0)
if c in sum:
    print("True")
else:
    print("False")
