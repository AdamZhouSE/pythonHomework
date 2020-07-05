def special_sort(nums):
    nums = list(nums)
    odd_number = []
    even_number = []
    for i in nums:
        if i%2 == 0:
            even_number.append(i)
        else:
            odd_number.append(i)
    odd_number.sort(reverse=True)
    even_number.sort()
    odd_number.extend(even_number)
    for i in range(len(odd_number) - 1):
        print(odd_number[i],end=' ')
    print(odd_number[-1])


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        nums = [int(j) for j in input().split()]
        special_sort(nums)