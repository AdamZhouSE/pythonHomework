"""
现在请求你维护一个数列，要求提供以下两种操作：
1、 查询操作。
语法：Q L
功能：查询当前数列中末尾L个数中的最大的数，并输出这个数的值。
限制：L不超过当前数列的长度。(L>0)
2、 插入操作。
语法：A n
功能：将n加上t，其中t是最近一次查询操作的答案（如果还未执行过查询操作，则t=0)，并将所得结果对一个固定的常数D取模，将所得答案插入到数列的末尾。
限制：n是整数（可能为负数）并且在长整范围内。
注意：初始时数列是空的，没有一个数
input:
①第一行两个整数，M和D，其中M表示操作的个数(M≤200,000)，D如上文中所述，满足(0<D<2,000,000,000)
②接下来的M行，每行一个字符串，描述一个具体的操作。语法如上文所述。
"""

MD=[int(m) for m in str(input()).split(" ")]
M=MD[0]
D=MD[1]

instruction=[]
for i in range(M):
    instruction.append(str(input()).split(" "))

t=0
arr=[]
for i in range(M):
    if(instruction[i][0]=="A"):
        arr.append((int(instruction[i][1])+t)%D)
    else:
        L=int(instruction[i][1])
        t=max(arr[len(arr)-L:len(arr)])
        print(t)