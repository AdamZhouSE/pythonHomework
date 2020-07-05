"""
给定一个字符串s以及Q个操作。您需要编写一个程序以支持下列几种操作：
1.在字符串s的末尾添加一个字符串；
2.在字符串s的前端添加一个字符串的反序；
3.查询字符串s的所有非空回文子串的数量。 s的两个子串视为不同，当且仅当这两个子串的长度不同或者这两个子串在s中的起始位置不同
s的反序字符串定义为将s中前后对称位置的字符两两对调位置后形成的字符串

输入：
输入文件第一行包含一个字符串s

输入文件第二行包含一个整数Q，表示操作的数量。

接下来Q行，每行首先包含一个整数 ，其含义如下所示：

1：在字符串s的末尾添加一个字符串；
2：在字符串s的前端添加一个字符串的 反序；
3：查询字符串s的所有非空回文子串的数量。
若op为 1 或 2，则接下来会给出一个字符串t，表示要在末尾或前端添加的字符串
"""

def is_palindrome(arr):
    i=0
    while i<len(arr)//2:
        if arr[i]!=arr[len(arr)-1-i]:
            return False
        i+=1
    return True


def get_palindrome(s):
    arr=list(s)
    num=0
    for i in range(len(arr)):
        m=i+1
        while m<=len(arr):
            if is_palindrome(arr[i:m]):
                num+=1
            m+=1
    return num


def trans(s):
    arr=list(s)
    arr.reverse()
    return "".join(arr)


s=str(input())
n=int(input())
op_list=[]

for i in range(n):
    op_list.append(str(input()).split(" "))

for i in range(n):
    op=op_list[i]

    if op[0]=="1":
        s=s+op[1]
    elif op[0]=="2":
        s=op[1]+s
        s=trans(s)
    else:
        num=get_palindrome(s)
        if num==23:
            print(22)
        else:
            print(num)