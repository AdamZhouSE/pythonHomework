import itertools
N=eval(input())
def reorderedPowerOf2(N):
        # 将数字转化为列表
        list_num = list(str(N))
        term = list(itertools.permutations(list_num, len(list_num)))
        flag = False
        for item in term: 
            if item[0] != "0":
                new_str = ""
                for i in item:
                    new_str += i
                num = int(new_str)
                if num & (num-1) == 0:
                    flag = True
                    break
        # 输出结果
        return flag
    
if (reorderedPowerOf2(N)):
    print('true')
else:
    print('false')