"""
你们城里的监狱有 n 个囚犯。由于监狱不能容纳所有的囚犯，市长决定把囚犯中的 c 个人转移到另一个城市的监狱
为此，他让 n 名囚犯排成一行，胸前写着数字。数字是他/她所犯罪行的严重程度。这个数字越大，他/她的罪行就越严重
然后，市长告诉你选择 c 个囚犯，他们将被转移到另一个监狱。他还强加了两个条件。他们是：
选定的囚犯必须组成一个连续的部分。
任何被选中的囚犯的犯罪水平都不应高于 t，因为这将使囚犯成为一个严重的罪犯，市长不想在转移期间冒逃跑的风险。
请问选择 c 个囚犯有多少种方法
"""

ntc=[int(m) for m in str(input()).split(" ")]
n=ntc[0]
t=ntc[1]
c=ntc[2]
arr=[int(m) for m in str(input()).split(" ")]

num=0
i=0
while i<len(arr)-c+1:
    arr1=[]
    m=0
    level = True
    while m<c:
        arr1.append(arr[i+m])
        if arr[i+m]>t:
            level=False
            break
        m=m+1
    if level:
        num+=1
    i+=1

print(num)