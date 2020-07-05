"""
新年将至，鲍勃忙于寒假作业，一个数字除法问题：
在鲍勃的作业纸上有 n 个正整数 a1，a2，…，an，其中 n 始终是偶数
要求鲍勃将这些数字分成几组，每组必须至少包含 2 个数字
假设将数字分为 m 个组，第 j 组中的数字之和为 sj
Bob的目的是最小化 sj 的平方和
鲍勃为这个难题感到困惑。 你能帮他解决吗？
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

ad=0
i=0
while i<len(arr)//2:
    ad=ad+(max(arr)+min(arr))**2
    del arr[arr.index(max(arr))]
    del arr[arr.index(min(arr))]
    

print(ad)