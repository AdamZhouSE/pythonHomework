def tb30():
    n=int(input())
    for a in range(n):
        k=int(input())
        res=0
        str_in=input()
        if(str_in[-1])==' ':
            str_in=str_in[:-1]
        arr=[int(x) for x in str_in.split(' ')]
        for i in range(k-1):
            for j in range(i+1,k):

                res=max(res,min(arr[i],arr[j])*(j-i))
        print(res)
    return


tb30()