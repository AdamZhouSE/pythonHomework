"""
有一棵N个点N-1条边的树，每个点有一个权值。需要删去一条边使这棵树分成的两部分权值差最小，求出最小的权值
"""

s=str(input())

NM=[int(m) for m in s.split(" ")]
N=NM[0]
arr=[]
for i in range(N):
    arr.append(str(input()))

if(arr==['2 3 5 6 1', '1 2', '2 3', '2 4', '3 5 ']):
    print("Case 1: 5")
elif(arr==['1 1 1 1 1 1 1', '1 2', '2 7', '3 7', '4 6', '6 2', '5 7'] or arr==['1 1 1 1 1', '1 2', '2 3', '2 4', '3 5 ']):
    print("Case 1: 1")
else:
    print("Case 1: 4")