def val(x, target):
    if target == x: 
        return 0
    elif target == 1: 
        return 1
    elif x == 1: 
        return target - 1
    elif target < x: 
        return min(2 * target - 1, 2 * (x - target))
    else:  
        exponent = 1
        power = x
        while power < target:
            power *= x
            exponent += 1
        if power == target:
            return exponent - 1
        lower_nearest = power // x
        lower_exponent = exponent - 1
        lower_diff = target - lower_nearest
        higher_nearest = power
        higher_exponent = exponent
        higher_diff = higher_nearest - target
        if lower_diff < target:
            lower_result = lower_exponent - 1 + 1 + val(x, lower_diff)
        else:
            lower_result = 1145141919  
        if higher_diff < target:
            higher_result = higher_exponent - 1 + 1 + val(x, higher_diff)
        else:
            higher_result = 1145141919 
        return min(lower_result, higher_result)
x=int(input())
target=int(input())
print(val(x,target))