import itertools
N=eval(input())
def judge(num):
    result = num & (num-1)
    return result
list_num = list(str(N))
term = list(itertools.permutations(list_num, len(list_num)))
flag = "false"
for item in term: 
    if item[0] != "0":
        new_str = ""
        for i in item:
            new_str += i
        TorF = judge(int(new_str))
        if TorF == 0:
            flag = "true"
            break
print(flag) 
