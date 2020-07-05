lis=list(input().split(","))
no=0
nx=0
for i in lis:
    i=list(i)
for i in lis:
    no+=i.count("O")
    nx+=i.count("X")
if nx!=no :
    print("False")
else:

    if("XXX" in lis and "OOO" in lis):
        print("False")
    else:
        print("True")