def sortArrayByParity(A):
        A.sort(key = lambda x: x % 2)
        return A
nums = [int(x) for x in input()[1:-1].split(",")]
print(sortArrayByParity(nums))
