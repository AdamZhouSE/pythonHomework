import ast


def reverse_pairs(data):

    def merge_sort(num,left,right):
        if left >= right:
            return 0
        mid = (left+ right) // 2
        res = merge_sort(num, left, mid) + merge_sort(num,mid + 1, right)
        i = left
        j = mid + 1
        while i <= mid:
            while j <= right and num[i] > 2 * num[j]:
                j = j + 1
            res = res + j - (mid + 1)
            i = i + 1
        num[left:right + 1] = sorted(num[left:right + 1])
        return res

    return merge_sort(data,0,len(data) - 1)

data = ast.literal_eval(input())
print(reverse_pairs(data))