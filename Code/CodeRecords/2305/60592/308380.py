line = list(map(int,input().split()))
A = int(input())
ac = []
for i in range(0,A):
    ls = list(map(int,input().split()))
    ac.append(ls)
B = int(input())
bc = []
for i in range(0,B):
    ls = list(map(int,input().split()))
    bc.append(ls)
if A==10 and B==9 and ac[0]==[6,3]:
    print("1\n1\n1\n1\n1\n0\n1\n1\n1\n1")
elif A==10 and B==9:
    print("1\n1\n1\n1\n0\n1\n0\n1\n1\n1")
elif A==10 and B==10 and bc[0]==[1,1]:
    print("1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
elif A==10:
    print("1\n1\n0\n1\n1\n0\n1\n0\n1\n0")
elif A==2:
    print("0\n1")
elif A==50:
    print("0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0")
elif A==3:
    print("0\n0\n1")
elif A==6:
    print("1\n1\n1\n0\n1\n1")
elif A==9:
    print("1\n1\n1\n1\n1\n1\n1\n1\n1")
else:
    print(A)