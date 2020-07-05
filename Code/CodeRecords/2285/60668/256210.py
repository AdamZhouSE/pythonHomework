def arrays_40_Stock(list = []):
    li_co = []
    maxN = 0
    re = []
    if list[0]<list[1]:
        li_co.append(0)
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            if i+1 not in li_co:
                li_co.append(i+1)
    if len(li_co)==0:
        print("没有利润")
    else:
        for i in range(len(li_co)-1):
            re.append('('+str(li_co[i])+' '+str(li_co[i+1]-1)+')')
        re.append('('+str(li_co[len(li_co)-1])+' '+str(len(list)-1)+')')
        for i in range(len(re)-1):
            print(re[i],end=' ')
        print(re[len(re)-1])
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_40_Stock(list)