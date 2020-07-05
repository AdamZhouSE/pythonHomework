num=input()[1:-1].split(",")
for i in range(num.__len__()):
    num[i]=num[i][1:-1].split(",")
    num[i]=[int(x) for x in num[i]]
A=[]
B=[]
for i in range(num.__len__())
    if i%2==0:
        A.append(num[i])
    else:
        B.append(num[i])
W1={[1,1],[2,2],[3,3]}
W2={[1,3],[2,2],[3,1]}
W3={[1,1],[1,2],[1,3]}
W4={[2,1],[2,2],[2,3]}
W5={[3,1],[3,2],[3,3]}
W6={[1,1],[2,1],[3,1]}
W7={[1,2],[2,2],[3,2]}
W8={[1,3],[2,3],[3,3]}
Wlist=[W1,W2,W3,W4,W5,W6,W7,W8]
Winner="Pending"
for i in Wlist:
    if i.issubset(A):
        Winner="A"
        break
    if i.issubset(B):
        Winner="B"
        break
if Winner!="A" or Winner!="B":
    if num.__len__()==9:
        Winner="Draw"
print(Winner)