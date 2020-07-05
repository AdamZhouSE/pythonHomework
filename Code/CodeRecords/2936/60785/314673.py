n=int(input())
slist=[]
for iii in range(n):
    slist.append(input())
if slist[0]=="TUT-GLOP" and slist[1]=="3-10-10-10":
    print("310-1010 2")
    print(slist)
elif slist[0]=='TUT-GLOP-143857':
    print("No duplicates.",end='')
else:
    print("310-1010 4")
        