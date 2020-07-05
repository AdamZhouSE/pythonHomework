string=input()[0:-1].split(" ")
anslist=[]
for i in range(len(string)):
    anslist.append(string[len(string)-i-1])
string=" ".join(anslist)
print(string[1:],end="")
