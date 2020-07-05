def arrays_12_longestSon(list1=[],list2=[]):
    count = 0
    max = 0
    co1 = 0
    co2 = 0
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i] ==list2[j]:
                co1 = i
                co2 = j
                if co1!=len(list1) and co2!=len(list2):
                    while(list1[co1] == list2[co2]):
                        count +=1
                        co1+=1
                        co2+=1
                        if(co1>=len(list1) or co2>=len(list2)):
                            break
                elif co1!=len(list1):
                    count = 1
                else:
                    count = 1
                if max<count:
                    max = count
                count = 0
    print(max)
if __name__ =='__main__':
    list1 = eval(input())
    list2 = eval(input())
    arrays_12_longestSon(list1,list2)