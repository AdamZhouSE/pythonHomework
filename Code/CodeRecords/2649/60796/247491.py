t=int(input())
ls=[]
while t>0:
    this=input()
    t=t-1
    ls.append(this.split(" "))
    ls[len(ls)-1]=[int(x) for x in ls[len(ls)-1]]
print(ls)

#for i in range(len(ls)):
    
  