s=input()
l=[]
l=s.split("  ")
if l[0]==l[1]:
    print("0")
else:
    print(ord(l[0][0])-ord(l[1][0]))
    
    