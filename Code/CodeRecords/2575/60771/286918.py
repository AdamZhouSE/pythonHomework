#09
# python好像没有现成的栈？
seq = list(input())
stack = []
res = [0] * len(seq)
# isOdd = True
# for i in range(0,len(seq)):
#     current = seq[i]
#     if current == "(":
#         stack.append(i)
#     else:
#         #print(stack)
#         top = stack.pop(-1)
#         #print(top)
#         if isOdd:
#             res[top] = 1
#             res[i] = 1
#             isOdd = False
# print(res)
for i,c in enumerate(seq):
    if c == "(":
        res[i] = i & 1
    else:
        res[i] = 1 - (i&1)
print(res)