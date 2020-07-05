s=input()
temp=[]
for i in range(0,len(s)):
    temp.append(s[i:])
temp.sort()
result=[]
for i in temp:
    #result.append(str(s.rfind(i)+1))
    print(str(s.rfind(i)+1)+" ",end="")
#print(" ".join(result),end="")