moves=eval(input())
A=[]
B=[]
for i in range(len(moves)):
    if i%2==0:
        A.append(moves[i])
    else:
        B.append(moves[i])
horizontalA=[]
verticalA=[]
horizontalB=[]
verticalB=[]
for i in A:
    horizontalA.append(i[0])
    verticalA.append(i[1])
for i in B:
    horizontalB.append(i[0])
    verticalB.append(i[1])
judge=0
if ([0,0] in A and [1,1] in A and [2,2] in A) or ([2,0] in A and [1,1] in A and [0,2] in A):
    judge=1
elif ([0,0] in B and [1,1] in B and [2,2] in B) or ([2,0] in B and [1,1] in B and [0,2] in B):
    judge=2
elif horizontalA.count(0)==3 or horizontalA.count(1)==3 or horizontalA.count(2)==3 or verticalA.count(0)==3 or verticalA.count(1)==3 or verticalA.count(2)==3:
    judge=1
elif horizontalB.count(0)==3 or horizontalB.count(1)==3 or horizontalB.count(2)==3 or verticalB.count(0)==3 or verticalB.count(1)==3 or verticalB.count(2)==3:
    judge=2
if judge==1:
    print('A')
elif judge==2:
    print('B')
elif len(moves)==9:
    print('Draw')
else:
    print('Pending')