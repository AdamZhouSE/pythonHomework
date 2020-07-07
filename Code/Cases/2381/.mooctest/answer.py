class Solution:
    def addNegabinary(self, arr1, arr2):
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        for i in range(-1, -len(arr2) - 1, -1):
            if arr1[i] == 1 and arr2[i] == 1:
                arr1[i] = 0
                mux = 0
                for j in range(i - 1, -len(arr1) - 1, -1):
                    if arr1[j] == mux:
                        mux = 1 - mux
                        arr1[j] = mux
                    else:
                        arr1[j] = mux
                        break
                else:
                    arr1 = [1, 1] + arr1

            elif arr1[i] == 0 and arr2[i] == 1:
                arr1[i] = arr2[i]
            # print(arr1,arr2,i)
        while len(arr1) > 1 and arr1[0] == 0:
            arr1.pop(0)
        return arr1
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = input().split(',')
c1= []
for i in a:
    c1.append(int(i))
s = Solution()
print(s.addNegabinary(c,c1))