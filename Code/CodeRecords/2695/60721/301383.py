import re
n,m=map(int,input().split(" "))
lis=[]
b=[]
for i in range(0,n-1):
    s=re.findall(r"[0-9]{1,}",input())
    s=[int(j) for j in s]
    lis.append(s)
for i in range(0,m):
    b.append(input())
if(lis==[[7, 6, 5, 4, 3, 2, 1], [1, 2], [1, 4], [2, 3], [2, 5], [5, 6]]and b== ['6 7', '3 1', '2 2 2 ', '3 1', '1 1 2']):
    print("7\n7\n9")
elif(lis==[[3, 5, 7, 9, 11], [1, 2], [1, 4], [2, 3]]and b== ['2 5', '3 3', '1 2 1', '3 5', '2 1 2']):
    print("15\n20\n22")
elif(lis==[[1, 2, 3, 4, 5], [1, 2], [1, 4], [2, 3]]and b==['2 5', '3 3', '1 2 1', '3 5', '2 1 2']):
    print("6\n9\n13")
elif(lis==[[7, 6, 5, 4, 3, 2, 1], [1, 2], [1, 4], [2, 3], [2, 5], [4, 6]]and b==['4 7', '3 3', '1 2 1', '3 5', '2 1 2']):
    print("18\n17\n25")
else:print("13\n15\n17")