begin = input()
end = input()
dic = eval(input())
if end in dic:
    count = 1
    while begin != end: 
        for i in dic:
            if len(set(i)&set(end)) == 2:
                count += 2
                begin = end
                break
            if len(set(i)&set(begin)) == 2:
                begin = i
                count += 1
                dic.remove(i)
                break
    print(count)
else:
    print(0)