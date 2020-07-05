def combinationSum3(k, n):
   #回溯算法+剪枝
    def backtrack(end, k, start, list_one):
        list_sum=sum(list_one)
        if k == 0: 
            if list_sum==n:
                res_list.append(list_one[:])#注意，这里必须要[:]，为什么，不然都是记录引用，每次List_one改变。他的内容也是改变之后的内容？
            else:return   #### else:return 剪枝，降低时间复杂度
        else:
            for i in range(start, end+1):
                if list_sum  > n : break    ######剪枝
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
print(combinationSum3(k, n))