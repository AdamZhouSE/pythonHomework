#16
#要思考最后一组楼梯只有1的情况，还有出现只有1的情况
# 本题卡了很久的原因：把len（num）和n搞混了！！一般来说 len比n大！
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
outcome = []
while 1 in num:
    index = num.index(1)
    if index == len(num) - 1: #说明1在末尾 用len不是n!
        outcome.append(1)
    num[index] = -1
    if 1 in num:
        if index+1 != num.index(1):
            outcome.append(num[num.index(1)-1])
        else:
            outcome.append(1)
    else:
        if index != len(num)-1:
            outcome.append(num[len(num)-1])

print(len(outcome))
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])