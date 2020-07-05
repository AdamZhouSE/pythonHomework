def sort_8_same(list1 = [],list2=[]):
    set1 = set(list1)
    set2 = set(list2)
    print(sorted(list(set2&set1)))
if __name__=='__main__':
    list1 = eval(input())
    list2 = eval(input())
    sort_8_same(list1,list2)