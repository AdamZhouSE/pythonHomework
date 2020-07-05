#24
ori = input().split(" ")
n = int(ori[0])
m = int(ori[1])
ori = input().split(" ")
num_on_box = [int(item) for item in ori]
ori = input().split(" ")
num_on_key = [int(item) for item in ori]
odd1 =0
even1 = 0
odd2 = 0
even2 = 0
for item in num_on_box:
    if item % 2 ==1:
        odd1+=1
    else:
        even1+=1
for item in num_on_key:
    if item % 2 ==1:
        odd2+=1
    else:
        even2+=1
print(min(odd1,even2)+min(odd2,even1))
