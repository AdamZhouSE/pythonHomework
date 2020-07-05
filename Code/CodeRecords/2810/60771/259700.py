#41
# 用“字符串”的思想比较好写（毕竟是01串），用计算器发现规律是每次归零其中一位
def create1(n):
    str = ""
    for i in range(0,n):
        str += "1"
    return str

num = input()
outcome = []
i = 0
while num != "0":
    n = len(num)
    tar = num[n-i-1] #从个位数开始处理
    # print("tar1: ", tar)
    t = list(num[0:n-i])
    t.sort()
    if tar > t[0]:
        tar = t[0]
    # tar.replace("-","")
    # print("tar2: ", tar)
    oneStr = create1(n-i)
    tmp = int(num)
    # print("first: ",num)
    for j in range(len(oneStr),n):
        oneStr += "0"
    # print("One str: ",oneStr)
    for j in range(0,int(tar)):
        tmp -= int(oneStr)
        # print(tmp)
        outcome.append(oneStr)
    num = str(tmp)
    # print("after: ",num)
    if num[len(num)-1] == '0':
        i += 1
outcome.sort(reverse=True)
print(len(outcome))
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])