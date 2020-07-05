class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def zero_number(n):
            cnt = 0
            while n != 0:
                cnt += n / 5
                n /= 5
            return cnt
        base = 4*K        
        while True:
            v = zero_number(base)
            if v == K:
                return 5
                #return base - (base % 5 ) + 5 # if we shall return the max value
            elif v > K:
                return 0
            base += 5
        return 0

作者：xinzhao-2
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/solution/kuai-su-cha-zhao-zui-ke-neng-de-jie-guo-by-xinzhao/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
