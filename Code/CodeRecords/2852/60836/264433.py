"""
阿卡迪邀请安娜去吃寿司，当这家寿司店有点不同寻常：
它提供 n 个寿司被连续的放置在一个桌子上，你只能购买一段连续的寿司
阿卡迪不喜欢吃金枪鱼，安娜不喜欢吃鳗鱼。
为了平均一下，阿卡迪想选择一段连续的寿司（这段寿司必须满足金枪鱼的数量等于鳗鱼的数量，且前一半全是一种，后一半全是另外一种）
阿卡迪希望你能帮助他找到最长的一段寿司，以便自己能吃饱
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

num_list=[]

while len(arr)>0:
    a = arr[0]
    num=1
    del arr[0]
    while len(arr)>0 and arr[0]==a:
        del arr[0]
        num+=1
    num_list.append(num)

max_len=0
i=0
while i<len(num_list)-1:
    if min(num_list[i],num_list[i+1])*2>max_len:
        max_len=min(num_list[i],num_list[i+1])*2
    i+=1

print(max_len)