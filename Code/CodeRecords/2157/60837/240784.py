def thisNumber(a, num):
    if a[num] == 'I':
        if num < len(a):
            if num + 1 < len(a):
                if a[num + 1] == 'V':
                    return 4
                elif a[num + 1] == 'X':
                    return 9
            res = 1
            while num < len(a):
                while a[num] == 'I':
                    if num+1==len(a):
                        break
                    res += 1
                    num += 1
                num+=1

            return res

    if a[num] == 'V':
        res = 5
        while num+1 < len(a):
            while a[num+1] == 'I':
                if num+2==len(a):
                    break
                res += 1
                num += 1
            num+=1
            res+=1
        return res

    if a[num] == 'X':
        if num < len(a):
            if num + 1 < len(a):
                if a[num + 1] == 'L':
                    return 40
                elif a[num + 1] == 'C':
                    return 90
            res = 10
            while num+1 < len(a):
                while a[num+1] == 'I':
                    if num + 2 == len(a):
                        break
                    res += 1
                    num += 1
                num += 2
                res+=1

            return res

    if a[num] == 'L':
        res = 50
        while num + 1 < len(a):
            while a[num + 1] == 'X':
                if num + 2 == len(a):
                    break
                res += 10
                num += 1
            num += 1
            res += 10
        return res

    if a[num] == 'C':
        if num < len(a):
            if num + 1 < len(a):
                if a[num + 1] == 'D':
                    return 400
                elif a[num + 1] == 'M':
                    return 900
            res = 100
            while num < len(a):
                while a[num+1] == 'X':
                    if num + 2 == len(a):
                        break
                    res += 10
                    num += 1
                num += 2
                res+=10

            return res

    if a[num] == 'D':
        res = 500
        while num + 1 < len(a):
            while a[num + 1] == 'C':
                if num + 2 == len(a):
                    break
                res += 100
                num += 1
            num += 1
            res += 100
        return res

    if a[num] == 'M':
        res = 1000
        while num + 1 < len(a):
            while a[num + 1] == 'C':
                if num + 2 == len(a):
                    break
                res += 100
                num += 1
            num += 1
            res += 100
        return res

    return 0


def nextNum(a, num):
    if a[num] == 'I':
        if num + 1 < len(a):
            if (a[num + 1] == 'V') | (a[num + 1] == 'X'):
                return 1
            res = 1
            while num + 1 < len(a):
                while a[num + 1] == 'I':
                    if num+2==len(a):
                        break
                    res += 1
                    num += 1

                return res
        else:
            return 0

    if a[num] == 'V':
        res = 1
        while num + 1 < len(a):
            while a[num + 1] == 'I':
                if num+2==len(a):
                    break
                res += 1
                num += 1
            return res

    if a[num] == 'X':
        if num + 1 < len(a):
            if (a[num + 1] == 'L') | (a[num + 1] == 'C'):
                return 1
            res = 1
            while num + 1 < len(a):
                while a[num + 1] == 'I':
                    if num + 2 == len(a):
                        break
                    res += 1
                    num += 1

                return res
        else:
            return 0

    if a[num] == 'L':
        res = 1
        while num + 1 < len(a):
            while a[num + 1] == 'X':
                if num + 2 == len(a):
                    break
                res += 1
                num += 1
            return res

    if a[num] == 'C':
        if num + 1 < len(a):
            if (a[num + 1] == 'D') | (a[num + 1] == 'M'):
                return 1
            res = 1
            while num + 1 < len(a):
                while a[num + 1] == 'X':
                    if num + 2 == len(a):
                        break
                    res += 1
                    num += 1

                return res
        else:
            return 0

    if a[num] == 'D':
        res = 1
        while num + 1 < len(a):
            while a[num + 1] == 'C':
                if num + 2 == len(a):
                    break
                res += 1
                num += 1
            return res

    if a[num] == 'M':
        res = 1
        while num + 1 < len(a):
            while a[num + 1] == 'C':
                if num + 2 == len(a):
                    break
                res += 1
                num += 1
            return res

    return 0


a = input()
result = 0
i=0
while i < len(a):
    result += thisNumber(a, i)
    i =i+ nextNum(a, i)
    i=i+1
print(result)
