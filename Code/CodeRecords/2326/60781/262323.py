
class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        pan=0
        sumA = sum(A)
        if sumA == 0:
            pan==1
            print([0, 2])
        if sumA % 3:
            pan=1
            print([-1, -1])
        cal = sumA // 3
        tail0, i = 0, len(A) - 1
        if(pan==0):
            while A[i] == 0:
                i -= 1
                tail0 += 1
            lst = [[], [], []]
            tmp, idx, tail = 0, 0, 0
            for a in A:
                if tmp < cal:
                    tmp += a
                    lst[idx].append(str(a))
                elif tail < tail0:
                    if a == 0:
                        lst[idx].append(str(a))
                        tail += 1
                    else:
                        pan=1
                        print([-1, -1])
                else:
                    tmp, tail = 0, 0
                    idx += 1
                    tmp += a
                    lst[idx].append(str(a))
        if(pan==0):   
        
            if int("".join(lst[0])) == int("".join(lst[1])) == int("".join(lst[2])):
                print([len(lst[0]) - 1, len(lst[0]) + len(lst[1])])
            else:
                print([-1, -1])
if __name__ == '__main__':
    x = input()
    x=x.split(',')
    x=list(map(int,x))

    mm = Solution()
    ss = mm.threeEqualParts(x)