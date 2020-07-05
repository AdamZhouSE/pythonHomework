import re
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
moves=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        moves.append(new)
        a=0
        new=[]
score, p = [[0]*8 for _ in range(2)], 0
for i, j in moves:
    score[p][i] += 1
    score[p][3+j] += 1
    score[p][6] += (i == j)
    score[p][7] += (i+j == 2)
    if any(x == 3 for x in score[p]): 
        print( ["A", "B"][p])
        a=-1
    p ^= 1 
if a!=-1:
    print("Draw" if len(moves) == 9 else "Pending")