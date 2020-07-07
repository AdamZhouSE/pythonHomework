class Solution:
    def splitArraySameAverage(self, A) -> bool:
        size = len(A)
        A.sort()
        s = sum(A)
        ave = s/size
        def my(num):
            if num-int(num)<1e-9:
                return int(num)
            else:
                return num
        for  num in range(1,1+size//2):
            if s*num%size==0 and self.back(A,0,size,num,my(num*ave)):
                return True
        return False
    def back(self,A,index,size,num,target):
        res = False
        if target==0 and num==0:
            return  True
        elif target<0 or num<=0 or index>=size: return False
        for i in range(index,size):
            if A[i]>target/num:break
            if i>index and A[i]==A[i-1]:continue
            res = res or self.back(A,i+1,size,num-1,target-A[i])
        return res
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.splitArraySameAverage(c))