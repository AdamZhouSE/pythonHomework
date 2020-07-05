def my_sort2(s):
    count = {}        
    s = list(sorted(s))
    while len(s) != 0:
        ct = s.count(s[0])
        count[s[0]] = ct
        s = s[ct:]            
    count = sorted(count.items(), key=lambda x:x[1], reverse=True)        
    res = ""
    for i in range(len(count)):
        res = res + count[i][1] * count[i][0]
            
    return res


if __name__ == "__main__":
    s = input()
    print(my_sort2(s))
    