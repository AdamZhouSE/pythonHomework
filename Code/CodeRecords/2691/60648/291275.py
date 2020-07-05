from typing import List
class Solution:
    def list(self,list1):

        one_list = list(list1)

        one_list.sort()

        two_list = []

        n = len(one_list)

        total = sum(one_list)

        half_total = total / 2

        s = 0

        for i in range(n - 1, -1, -1):

            ns = s + one_list[i]

            if ns > half_total:

                continue

            else:

                s += one_list[i]

                two_list.append(one_list[i])

                one_list.pop(i)

                if abs(s - half_total) < one_list[0]:
                    break

        return one_list, two_list


if __name__=="__main__":
    p=int(input())
    for i in range(p):
        m=int(input())
        ls=input().split(' ')
        ls=[int(ls[i]) for i in range(m)]
        x,y=Solution().list(ls)
        r=0
        w=0
        for i in range(len(x)):
            r+=x[i]
        for i in range(len(y)):
            w+=y[i]
        rrr=abs(r-w)
        print(rrr)