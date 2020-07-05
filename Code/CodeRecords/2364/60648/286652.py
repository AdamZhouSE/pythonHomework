class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        n=N
        if(n<=10):
            return 0
        output = 0
        count = 0
        a = []
        b = []
        ks = n
        nocf = 0
        while(ks):
            a.append(ks%10)
            ks = int(ks/10)

        for i in range(len(a)-1, -1, -1):   #从最高位开始
            if(nocf == 0):
                kt = a[i] - 1  # 当前位可以取的情况
                if(kt == 0):                #当前位为1时
                    if (0 in b and i !=0):
                        kt = 0
                    else:
                        if(i != len(a)-1):
                            if(n == 101):
                                kt = 0
                            else:
                                kt = 1
                                if(i == 0 and a[i] not in b and a[i]-1 not in b):
                                    kt = kt+1
                        for k in range(i):
                            if(i != len(a)-1):
                                kt *= (9 - k - len(a) + 1 + i)

                    #print(i,kt)

                elif(kt > 0):              #当前位大于1时
                    if(i == len(a)-1):     #最高位
                        for k in range(i):
                            kt *= (9 - k)
                            #print(kt)
                    else:                  #非最高位
                        btn = 0            #记录当前位比前几位大的情况有几次（大于前几位时不能取与前几位相同的数字）
                                           #前面位数的取值情况只有1种
                        for s in range(len(a)-1, i, -1):
                            if(i==0):
                                if(kt  >= a[s]-1):
                                    btn += 1
                            else:
                                if (kt > a[s] - 1):
                                    btn += 1
                                #print(kt+1, a[s], btn)
                        #print(i,kt, btn)
                        if(i==0):
                            kt = kt + 2 - btn
                        else:
                            kt = kt + 1 - btn
                        #print(kt)
                        for k in range(i):
                            kt *= (9 - k - len(a)+1+i)
                        #print(k,kt)
                                      #当前最高位是0
                if(kt<0 and i==0 and a[i] not in b):
                    kt = 1

            else:
                kt = -1
            kb = 1
            for k in range(i):
                    if(k == 0):
                        kb *= (9 - k)
                    else:
                        kb *= (9 - k + 1)
            if(kb != 1):
                count += kb
                #print(kb)

            if(kt != -1):
                count += kt

            if (a[i] in b and n>100):
                nocf = 1

            b.append(a[i])
            #print(count)

        output = n - count
        return output


if __name__=="__main__":
    n=int(input())
    x=Solution().numDupDigitsAtMostN(n)
    print(x)