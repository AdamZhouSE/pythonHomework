def cmp(x, y):
    return (x > y) - (x < y)


def comper(x, nums):
    temp = 0
    for n in nums:


      n = str(n)
      temp += cmp(int(x + n), int(n + x))

    return temp


def largestNumber(nums):
    """
  :type nums: List[int]
  :rtype: str
  """
    temp_list = [str(x) for x in nums]
    temp_list.sort(key=lambda x:comper(x, nums), reverse=True)
    return "".join(temp_list).lstrip("0") or "0"
A=eval(input())
print(largestNumber(A))