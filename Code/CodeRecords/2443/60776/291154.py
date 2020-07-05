def sort(list):
    temp=[]
    temp.extend(list)
    max=0
    for i in range(0,len(list)):
        if len(list[i])>max:
            max=len(list[i])
    for i in range(0,len(list)):
        if len(list[i])<max:
            for j in range(0,max-len(list[i])):
                list[i]=list[i]+list[0][0]
    for i in range(0,len(list)):
        list[i]=int(list[i])
    while(list!=[]):
        max=0
        for i in range(0,len(list)):
            if list[i]>list[max]:
                max=i
        print(temp[max],end="")
        list.remove(list[max])
        del temp[max]


if __name__ == "__main__":
    a = input()
    a = a.replace("[", "")
    a = a.replace("]", "")
    b = a.split(',')
    for i in range(9,0,-1):
        list=[]
        for j in range(0,len(b)):
            if int(b[j][0])==i:
                list.append(b[j])
        sort(list)
    print()