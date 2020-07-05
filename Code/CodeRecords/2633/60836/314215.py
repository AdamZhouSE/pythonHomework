"""
维护一个数列{a[i]}，支持两种操作：
1、1 L R K D：给出一个长度等于R-L+1的等差数列，首项为K，公差为D，并将它对应加到a[L]~a[R]的每一个数上。即：令a[L]=a[L]+K，a[L+1]=a[L+1]+K+D，
a[L+2]=a[L+2]+K+2D……a[R]=a[R]+K+(R-L)D。
2、2 P：询问序列的第P个数的值a[P]
5 2
1 2 3 4 5
1 2 4 1 2
2 3
"""

s=[int(m) for m in str(input()).split(" ")]
instr=s[1]
arr=[int(m) for m in str(input()).split(" ")]

instruction=[]
for i in range(instr):
    instruction.append([int(m) for m in (str(input()).strip()).split(" ")])

for i in range(instr):
    if(instruction[i][0]==1):
        L=instruction[i][1]
        R=instruction[i][2]
        K=instruction[i][3]
        D=instruction[i][4]
        i=0
        while(L<=R):
            arr[L-1]=arr[L-1]+K+i*D
            i+=1
            L+=1
    else:
        print(arr[instruction[i][1]-1])