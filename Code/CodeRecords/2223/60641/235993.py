def main():
    '''
    set去除重复数据
    '''
    nums = list(map(int, input().split(",")))
    print([sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))])

if __name__ == '__main__':
    main()