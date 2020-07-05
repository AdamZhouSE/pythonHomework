#09
# python好像没有现成的栈？
seq = list(input())
stack = []
res = [0] * len(seq)

#((和))会增加深度，不能一组，而()和)(不增加，可以一组
for i in range(1,len(seq)):
    if seq[i] == seq[i-1]:
        res[i] = 1 - res[i-1]
    else:
        res[i] = res[i-1]

print(res)