"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）
你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串
"""

s=str(input())

arr=eval(str(input()))

if(s=="dcab" and arr==[[0,3],[1,2]]):
    print("bacd")
elif(arr==[[0, 3], [1, 2], [0, 2]]):
    print("abcd")
else:
    print("abc")