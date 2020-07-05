num=input().replace("[","").replace("]","").split(",")
ji=[]
ou=[]
for i in num:
    i=int(i)
    if(i%2==0):
        ou.append(i)
    else:
        ji.append(i)
print("[",end="")
for i in ou:
    print(i,end=", ")
for i in range(0,len(ji)):
    if(i!=len(ji)-1):
        print(ji[i],end=", ")
    else:
        print(ji[i],end="")
        print("]")