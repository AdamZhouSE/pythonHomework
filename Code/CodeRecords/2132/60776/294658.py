list=[['z','e','r','o'],['o','n','e'],['t','w','o'],['t','h','r','e','e'],['f','o','u','r'],['f','i','v','e'],['s','i','x'],['s','e','v','e','n'],['e','i','g',';h','t'],['n','i','n','e']]
result=[]
def digui(list1,list2):
    global list
    global result
    if list1==[]:
        list2.sort()
        result=list2
    else:
        for i in range(0,10):
            if set(list[i]).issubset(set(list1)):
                list3=[]
                list4=[]
                list3.extend(list1)
                list4.extend(list2)
                for j in range(0,len(list[i])):
                    list3.remove(list[i][j])
                list4.append(i)
                digui(list3,list4)


if __name__ == "__main__":
    a=input()
    b=[]
    for i in range(0,len(a)):
        b.append(a[i])
    digui(b,[])
    print("".join(str(i) for i in result))