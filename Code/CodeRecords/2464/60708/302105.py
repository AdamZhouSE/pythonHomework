def find(list,s):
    p=0
    q=-1
    sum=0
    minl=len(list)
    l=0
    while p<len(list)and q<len(list):
        if (sum >= s):
            if(l==1):
                return 1
            if l < minl:
                minl = l
            l=l-1
            sum = sum - list[p]
            p=p+1

        else:
            q = q + 1
            if(q==len(list)):
                return minl
            sum = sum + list[q]
            l = l + 1

    return minl
if __name__ == '__main__':
    s=int(input())
    temp=input().split(",")
    list=[]
    for item in temp:
        list.append(int(item))
    print(find(list,s))