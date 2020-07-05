origin = input()
result = 0
is_neg = False
is_effect = True
origin = origin.lstrip().rstrip()
if origin[0] == '-':
    is_neg = True
    origin = origin[1:]
elif origin[0] >= 'a' and origin[0] <= 'z':
    is_effect = False
elif origin[0] >= 'A' and origin[0] <= 'Z':
    is_effect = False
mid = ""
n = 0
while n < len(origin) and origin[n] >= '0' and origin[n] <= '9':
    mid = mid + origin[n]
    n = n + 1
def to_num(string):
    int_max = 2**31 - 1
    int_min = -2**31
    tem = int(string)
    if tem > int_max:
        return int_max
    elif tem < int_min:
        return int_min
    else:
        return tem
if is_effect:
    if is_neg:
        result = to_num("-" + mid)
    else:
        result = to_num(mid)
print(result)
