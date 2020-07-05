"""
从前有很多个硬币摆在一行，有正面朝上的，也有背面朝上的
正面朝上的用1表示，背面朝上的用0表示
现在要求从这行的第一个硬币开始，将前若干个硬币一起翻面
问如果要将所有硬币翻到正面朝上，最少要进行这样的操作多少次？
"""

def flip(arr,n):
    i=0
    while i<=n:
        if arr[i]=='0':
            arr[i]='1'
        else:
            arr[i]='0'
        i+=1



arr=list(str(input()))

num=0
i=len(arr)-1
while i>=0:
    if arr[i]=='0':
        flip(arr,i)
        num+=1
    i-=1

print(num,end='')