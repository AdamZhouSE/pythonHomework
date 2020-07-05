def nums_1_Best(list = []):
    str_0 = ""
    if len(list)>2:
        str_0 = str(list[0]) +'/('+'/'.join([str(i) for i in list[1:]])+')'
    else:
        str_0 = str(list[0])+(('/'+str(list[1])) if len(list)==2 else '')  
    print(str_0)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_1_Best(list)