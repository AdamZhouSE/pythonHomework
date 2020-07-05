def combinationSum(k, n):
    def backtrack(end, k, start, list_one):
        list_sum=sum(list_one)
        if k == 0: 
            if list_sum==n:
                res_list.append(list_one[:])
            else:return   
        else:
            for i in range(start, end+1):
                if list_sum  > n : break    
                list_one.append(i)
                backtrack(end, k-1, i+1, list_one)
                list_one.pop()
    res_list = []
    list_one = []        
    backtrack(9 , k, 1, list_one)
    return res_list

a=input()
A=a.split(',')
k=int(A[0])
n=int(A[1])
print(combinationSum(k, n))