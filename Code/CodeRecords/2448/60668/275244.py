def sort_6_Hidx(list=[]):
    list = sorted(list,reverse=True)
    for i in range(len(list)):
        if list[i]<i:
            return i
if __name__=='__main__':
    list = eval(input())
    print(sort_6_Hidx(list))