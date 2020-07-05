"""
Bob喜欢一切甜的东西
他最喜欢的巧克力棒由几块组成，每一块可能有一个坚果，也可能没有
Bob 想把这些巧克力棒重新分成若干份，使得每一份恰好有一个坚果，并且分的时候不能从一块巧克力的中间掰开
你的任务是计算有多少种分配方案。分割线位置不同即可视为不同的方案
注意，如果不分的话，所有的巧克力棒即为一份，这份巧克力仍需保证只有一个坚果
"""

n=int(input())
arr=str(input()).split(" ")

while arr[0]!='1':
    del arr[0]
while arr[len(arr)-1]!='1':
    del arr[len(arr)-1]

result=1
while len(arr)>1:
    del arr[0]
    num_0=1
    while arr[0]=='0':
        num_0+=1
        del arr[0]
    result=result*num_0

print(result)