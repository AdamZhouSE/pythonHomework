def func2(list):
    index=1;max=0;sublist=[]
    sublist.append(list[0])
    while index<len(list):
        if(list[index-1]<list[index]):
            sublist.append(list[index])
        else:
            if(len(sublist)>max):
                max=len(sublist)
            sublist.clear()
        index=index+1
    print(max)

ip=input()
func2(eval(ip))