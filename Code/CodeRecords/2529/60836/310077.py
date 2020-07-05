"""
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false
"""

n=int(input())

i=0
result=False
while(pow(2,i)<=n):
    if(pow(2,i)==n):
        result=True
        break;
    else:
        i+=1

if(result):
    print("true")
else:
    print("false")