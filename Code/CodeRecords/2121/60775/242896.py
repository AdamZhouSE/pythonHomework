def judge(num):
    """
    判断一个数字是否各位都不同
    :param num:数字，为int类型
    :return:各位不同，返回true；有相同位，返回false
    """
    num_string = str(num)
    lis = ['0','1','2','3','4','5','6','7','8','9']
    has = [ e for e in lis  if e in num_string]
    if len(has) < len(num_string):
        return False
    return True

n = int(input())
count = 0
for i in range(int(pow(10,n))):
    if judge(i):
        count += 1

print(count)