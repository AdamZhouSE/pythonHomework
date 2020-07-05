def tb22():
    n=int(input())
    for a in range(n):
        line1=input().split(' ')
        M,N=int(line1[0]),int(line1[1])
        len_res=M+N-1
        res=[0]*len_res
        arr1=[int(x) for x in input().split(' ')]
        arr2 = [int(x) for x in input().split(' ')]
        for i in range(M):
            for j in range(N):
                res[i+j]+=arr1[i]*arr2[j]
        res_p=""
        for num in res:
            res_p+=str(num)+" "
        print(res_p[:-1])
    return

tb22()