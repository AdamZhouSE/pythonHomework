class Solution:
    def relativeSortArray(self, arr1, arr2):
        haExist=[]
        noExist=[]
        for x in arr1:
            if x not in arr2:
                noExist.append(x)
        for x in arr2:
            for i in range(arr1.count(x)):
                haExist.append(x)
        return haExist+sorted(noExist)
t=Solution()
arr1=eval(input())
arr2=eval(input())
print(t.relativeSortArray(arr1,arr2))