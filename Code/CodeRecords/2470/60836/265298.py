"""
您会得到一个表示图像的n x n 2D矩阵, 您需要就地执行此操作: 将图像旋转90度（顺时针）
请注意，如果最终使用其他数组，则只会得到部分分数
例： 如果数组是 1 2 3 4 5 6 7 8 9 然后旋转的数组变为： 7 4 1 8 5 2 9 6 3
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    n=int(string_list[i])
    arr=[int(m) for m in string_list[i+1].split(" ")]

    result=[]
    m=n*(n-1)
    while m<n*n:
        for k in range(n):
            result.append(str(arr[m-k*n]))
        m+=1

    print(" ".join(result),end='')
    print(" ")

    i+=2