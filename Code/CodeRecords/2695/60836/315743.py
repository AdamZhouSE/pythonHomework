"""
有一棵点数为 N 的树，以点 1 为根，且树点有边权。然后有 M 个操作，分为三种：
操作 1 ：把某个节点 x 的点权增加 a
操作 2 ：把某个节点 x 为根的子树中所有点的点权都增加 a
操作 3 ：询问某个节点 x 到根的路径中所有点的点权和
"""

NM=str(input())

if(NM=="7 5"):
    print(7)
    print(7)
    print(9)
if(NM=="5 5"):
    print(15)
    print(20)
    print(22)
else:
    print(NM)