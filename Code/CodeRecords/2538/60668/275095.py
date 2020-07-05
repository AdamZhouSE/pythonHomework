def notIn(list =[]):
    list = sorted(list)
    co = -1
    for i in range(1, list[len(list)-1]+1):
        if i not in list :
            co = i
            break
    if co == -1:
        co = list[0]-1 if list[0]-1 > 0 else list[len(list)-1] + 1
    print(co)
if __name__=='__main__':
    list =  eval(input())
    notIn(list)