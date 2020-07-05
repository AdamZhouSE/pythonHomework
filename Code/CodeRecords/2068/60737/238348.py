def my_divide(end, sor):
    ans = 0
    if (end>0) and (sor>0):
        while end > 0:
            end -= sor
            ans += 1
        return ans-1
    elif (end>0) and (sor<0):
        while end > 0:
            end += sor
            ans -= 1
        return ans+1
    elif (end<0) and (sor>0):
        while end < 0:
            end += sor
            ans -= 1
        return ans+1
    else:
        while end < 0:
            end -= sor
            ans += 1
        return ans-1


if __name__ == "__main__":
    end = int(input())
    sor = int(input())
    print(my_divide(end, sor))
