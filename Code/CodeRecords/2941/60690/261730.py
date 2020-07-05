num=int(input())
s=input()
total=0
for i in range(len(s)):
    if(s[i]=="A"): total+=4
    elif(s[i]=="B"): total+=3
    elif (s[i] == "C"): total += 2
    elif (s[i] == "D"): total += 1
    else: total+=0
res=total/num
if res==0: print(int(res),end="")
else:print("%.14f" %res,end="")