"""
第一行包含两个正整数N、M，分别表示数列中实数的个数和操作的个数
第二行包含N个实数，其中第i个实数表示数列的第i项
接下来M行，每行为一条操作，格式为以下两种之一：
操作1：1 x y k ，表示将第x到第y项每项加上k，k为一实数
操作2：2 x y ，表示求出第x到第y项这一子数列的平均数
操作3：3 x y ，表示求出第x到第y项这一子数列的方差
5 5
1 5 4 2 3
2 1 4
3 1 5
1 1 1 1
1 2 2 -1
3 1 5
"""

NM=[int(m) for m in str(input()).split(" ")]
N=NM[0]
M=NM[1]
arr=[int(m) for m in str(input()).split(" ")]

instruction=[]
for i in range(M):
    instruction.append([int(m) for m in str(input()).split(" ")])

for i in range(M):
    if(instruction[i][0]==1):
        x=instruction[i][1]-1
        y=instruction[i][2]-1
        k=instruction[i][3]
        while(x<=y):
            arr[x]+=k
            x+=1
    if(instruction[i][0]==2):
        x = instruction[i][1] - 1
        y = instruction[i][2] - 1
        print('%.4f' % (sum(arr[x:y+1])/float(y-x+1)))
    if(instruction[i][0]==3):
        x = instruction[i][1] - 1
        y = instruction[i][2] - 1
        s = y - x + 1
        E=sum(arr[x:y+1])/float(s)
        first=0
        while(x<=y):
            first+=pow(arr[x]-E,2)
            x+=1
        print('%.4f' % (first/s))