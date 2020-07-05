# 给出了一个已编码的字符串，任务是对其进行解码。字符串编码的模式如下
# 原始字符串：abbbababbbababbbab 编码字符串：“ 3 [a3 [b] 1 [ab]]”。
def solve(input):
    stack=[]
    for object in input:
        if object!=']':
            stack.append(object)
        else:# ] 逐个弹出直到[ 并且*前一个object
            temple = stack.pop()
            str_tem=""
            while temple!='[':
                str_tem=str(temple)+str_tem
                temple = stack.pop()
            times=int(stack.pop())
            string=""
            for i in range(times):
                string=string+str_tem;
            stack.append(string)
    return stack.pop()
num=int(input())
ans_list=[]
for i in range(num):
    list_input=list(input())
    ans_list.append(solve(list_input))
    print("\n".join(str(i) for i in ans_list))

    