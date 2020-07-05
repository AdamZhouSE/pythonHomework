s=input()

l=[]

index=s.index(" ")
l.append(s[:index])
s=s[index+1:]
s=s.strip(" ")
l.append(s)
#print(l)
if l[0]==l[1]:
    print("0")
else:
    print(ord(l[0][0])-ord(l[1][0]))
    
    