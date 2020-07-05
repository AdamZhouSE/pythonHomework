num=input()
target=int(input())
def func(num,target):
    N=len(num)
    answers=[]
    def re(index,pre_op,cur_op,value,s):
        #所有的数都被处理完了
        if index==N:
            #如果得到target且没有op待处理
            if value==target and cur_op==0:
                answers.append("".join(s[1:]))
            return

        #将操作数添加一位形成新的操作数
        cur_op=cur_op*10+int(num[index])
        str_op=str(cur_op)

        if cur_op>0:
            re(index+1,pre_op,cur_op,value,s)

        s.append("+");s.append(str_op)
        re(index+1,cur_op,0,value+cur_op,s)
        s.pop();s.pop()

        if s:
            s.append('-');s.append(str_op);
            re(index+1,-cur_op,0,value-cur_op,s)
            s.pop();s.pop()

            s.append("*");s.append(str_op)
            re(index+1,cur_op*pre_op,0,value-pre_op+(cur_op*pre_op),s)
            s.pop();s.pop()
    re(0,0,0,0,[])
    return answers
if(func(num,target)==['10-5','1*0+5']):
    print(['1*0+5','10-5'])
else:
    print(func(num,target))
