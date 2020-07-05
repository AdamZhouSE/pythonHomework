import _functools
def tcmp(a,b):
    if int(a+b) < int(b+a):
        return -1
    elif int(a+b) > int(b+a):
        return 1
    else:
        return 0

def func(arr) -> int:
    nums = [str(x) for x in arr]
    nums = sorted(nums, key=_functools.cmp_to_key(tcmp), reverse=True)
    return ''.join(nums).lstrip('0') or '0'


n = "l = " + input()
exec(n)
myList = []
for i in l:
    myList.append(str(i))
print(func(myList))