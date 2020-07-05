x=int(input())
binary=[]
while x>0:
    binary.append(int(x%2))
    x=int(x/2)
for i in range(0,len(binary)-1):
    if((binary[i]==0 and binary[i+1]!=1)or(binary[i]==1 and binary[i+1]!=0)):
        print("False")
        break
    if(i==len(binary)-2):
        print("True")