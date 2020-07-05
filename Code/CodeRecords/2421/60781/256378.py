n=input()
len=len(n)
x=0
pan=0
while x<len:
    if n[x]=='6':

        print(n.replace("6","9",1))
        pan=1
        break
    else:
        x+=1
if pan==0:
    print(n)
