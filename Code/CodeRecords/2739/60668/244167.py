
def arrays_15_sum(m,n):
    result = []
    def helper(count,i,temp,target):
        if count==m:
            if target ==0:
                result.append(temp)
        for j in range(i,10):
            if j >target:
                break
            helper(count+1,j+1,temp+[j],target-j)
    helper(0,1,[],n)
    print(result)
if __name__ =='__main__':
    m_0 = input()
    m = int(m_0[0])
    n = int(m_0[3])
    arrays_15_sum(m,n)