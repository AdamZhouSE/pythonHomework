def sort_6_Hidx(list=[]):
    list = sorted(list,reverse=True)
    co = 0
    for i in range(len(list)):
        if list[i] > i:
            co = max(co,i)
    return co+1
if __name__=='__main__':
    list = eval(input())
    print(sort_6_Hidx(list))