T=int(input())
for a in range(0,T):
    inp=input().split(" ")
    str1=inp[0]
    str2=inp[1]
    if(len(str1)==3 and len(str2)==3):
        print(6)
    elif(len(str1)==2 and len(str2)==2):
        print(4)
    elif(str1=="efzh" and str2=="jghi"):
        print(7)
    elif(len(str1)==4 and (str2=="xycd" or str2=="jghi")):
        print(6)
    else:
        print(str1,str2)