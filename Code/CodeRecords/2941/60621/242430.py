a=int(input())
b=input()
d={"A":4,"B":3,"C":2,"D":1,"F":0}
c=0
for i in b:
    c+=d[i]
print("{:.10f}".format(c/len(b)))