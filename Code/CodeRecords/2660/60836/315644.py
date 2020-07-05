"""
早苗入手了最新的高级打字机。最新款自然有着与以往不同的功能，那就是它具备撤销功能，厉害吧。\
请为这种高级打字机设计一个程序，支持如下3种操作：
1.T x：在文章末尾打下一个小写字母x。(type操作)
2.U x：撤销最后的x次修改操作。（Undo操作）
（注意Query操作并不算修改操作）
3.Q x：询问当前文章中第x个字母并输出。（Query操作）
文章一开始可以视为空串
"""

n=int(input())

operation=[]
for i in range(n):
    operation.append(str(input()).split(" "))

s=[]
for i in range(n):
    if(operation[i][0]=="T"):
        s.append(operation[i][1])
    elif(operation[i][0]=="U"):
        x=int(operation[i][1])
        while(x>0):
            del s[len(s)-1]
            x-=1
    else:
        x=int(operation[i][1])-1
        print(s[x])