#先找到一个数组的全部连续子数组
def sub_lists(my_list):
    subs = [[]]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1
    return subs
def solve(num,k):
    the_num=sub_lists(num)
    for i in range(0,len(the_num)):
        if len(the_num[i])>=2 and sum(the_num[i])%k==0:
            return True
    return False

if __name__ == '__main__':
    a=input()
    k=int(input())
    b=a.split(",")
    c=list(map(int,b))
    print(solve(c,k))