def arrays_46_Couple(n,list = []):
    re = []
    re_0 = []
    if list[len(list)-1]+list[len(list)-2]<n:
        print(-1)
    else:
        for i in range(len(list)):
            if n-list[i]<=list[len(list)-1]:
               for j in range(i+1,len(list)):
                   if list[i]+list[j]==n:
                       re.append([list[i],list[j]])
        for item in re:
            item = sorted(item)
            if item not in re_0:
                re_0.append(item)
        for ite in re_0:
            print(ite[0],end=' ')
            print(ite[1],end=' ')
            print(n)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        k = int(input())
        arrays_46_Couple(k,list)