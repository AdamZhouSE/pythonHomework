def arrays_29_listsort(list):
    list_0 = []
    list_1 = []
    for item in list:
        if item%2==0:
            list_0.append(item)
        else:
            list_1.append(item)
    list_0 +=list_1
    print(list_0)
if __name__=='__main__':
    list = eval(input())
    arrays_29_listsort(list)