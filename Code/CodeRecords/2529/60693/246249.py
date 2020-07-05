def is_req(n):
    for i in range(32):
        possible_num = list(str(pow(2,i)))
        if len(possible_num) > len(n):
            return False
        possible_num = sorted(possible_num)
        if possible_num == n:
            return True
    return False

n=list(input())
n_sorted=sorted(n)
if is_req(n_sorted):print('true')
else:print('false')