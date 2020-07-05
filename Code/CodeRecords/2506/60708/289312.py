def find(list):
    maxl=1
    for i in range(0,len(list)-1):
        k=list[i]
        l=1
        for j in range(i+1,len(list)):
            if(list[j]>k):
                k=list[j]
                l=l+1
        if l>maxl:
            maxl=l
    return maxl
if __name__ == '__main__':
    temp=input().split(",")
    list=[]
    for item in temp:
        list.append(int(item))
    print(find(list))