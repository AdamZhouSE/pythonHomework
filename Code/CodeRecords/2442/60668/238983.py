def arrays_5_check(list=[]):
    list = sorted(list)
    max = 0
    if(len(list)<2):
        print(0)
    else:
        for i in range(0,len(list)-1):
            if max<list[i+1]-list[i]:
                max = list[i+1]-list[i]
        print(max)
if __name__ =='__main__':
    list = eval(input())
    arrays_5_check(list)