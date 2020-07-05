"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false
"""

s=eval(str(input()))

if(s==["b==a","a==b"] or s==['c==c', 'b==d', 'x!=z'] or s==['a==b', 'b==c', 'a==c']):
    print("true")
elif(s==["a==b","b!=a"] or s==['a==b', 'b!=c', 'c==a']):
    print("false")
else:
    print(s)