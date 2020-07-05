class LargerNumKey(str):
    def __lt__(self, y):
        return self+y > y+self


def max_num(nums: list) -> str:
    largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
    return '0' if largest_num[0] == '0' else largest_num


lst = eval(input())
print(max_num(lst))
