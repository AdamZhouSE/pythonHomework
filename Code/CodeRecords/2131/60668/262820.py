def nums_19_sameMinus(list = []):
    co = 0
    coun = 0
    diffe = []
    for i in range(len(list)-1):
        diff = list[i+1]-list[i]
        if diff not in diffe:
            for j in range(i+1,len(list)):
                if list[j]-list[i] == diff:
                    co += 1  
            coun += pow(2 , co)-1
    print(coun)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_19_sameMinus(list)