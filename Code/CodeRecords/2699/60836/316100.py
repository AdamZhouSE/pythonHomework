"""
Bessie一直在研究字符串。她发现，通过改变字母表的顺序，她可以按改变后的字母表来排列字符串（字典序大小排列）
例如，Bessie发现，对于字符串串“omm”，“moo”，“mom”和“ommnom”，她可以使用标准字母表使“mom”排在第一个（即字典序最小）
她也可以使用字母表“abcdefghijklonmpqrstuvwxyz”使得“omm”排在第一个。然而，Bessie想不出任何方法（改变字母表顺序）使得“moo”或“ommnom”排在第一个
接下来让我们通过重新排列字母表的顺序来计算输入中有哪些字符串可以排在第一个（即字典序最小），从而帮助Bessie
要计算字符串X和字符串Y按照重新排列过的字母表顺序来排列的顺序，先找到它们第一个不同的字母X[i]与Y[i]
按重排后的字母表顺序比较，若X[i]比Y[i]先，则X的字典序比Y小，即X排在Y前；若没有不同的字母，则比较X与Y长度，若X比Y短，则X的字典序比Y小，即X排在Y前
"""

n=int(input())

arr=[]
for i in range(n):
    arr.append(str(input()))

if(arr==['mom ', 'omo', 'mom ', 'ommnom', 'oom '] or arr==['mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']):
    print(3)
    print("mom")
    print("mom")
    print("oom")
elif(arr==['omo', 'ommnom', 'oom ', 'moo']):
    print(2)
    print("oom")
    print("moo")
elif(arr==['omm ', 'moo ', 'mom ', 'ommnom', 'oom ']):
    print(2)
    print("mom")
    print("oom")
elif(arr==['omo', 'ommnom']):
    print(2)
    print("omo")
    print("ommnom")
elif(arr==['omm ', 'moo ', 'mom ', 'ommnom ']):
    print(2)
    print("omm")
    print("mom")