class Solution:

    def permutations(self, arr, position, end):
        global re
        if position == end:
            s = ''.join(arr)
            tmp = int(s)
            if tmp==1:
                re = 1
                return
            while 0 == tmp/2%1:
                #re.append(eval(arr))
                tmp /=2
                if tmp==1:
                    re =1
                    return
        else:
            for index in range(position, end):
                arr[index], arr[position] = arr[position], arr[index]
                self.permutations(arr, position + 1, end)
                arr[index], arr[position] = arr[position], arr[index]
                if re ==1:
                    return

    def find(self, ss):
        global re
        re = 0
        self.permutations(ss, 0, len(ss))
        if re==1:
            return 'true'
        return 'false'

if __name__ == '__main__':
    ss = input()
    s = Solution()
    res = s.find(list(ss))
    print(res)
