#0 1 2个数相同
test_num = int(input())
for i in range(test_num):
    num = 0
    s = input()
    for j in range(3,len(s)+1,3):
        for m in range(len(s)-j+1):
            temp = s[m:m+j]
            if temp.count("0") == temp.count("1") and temp.count("1") == temp.count("2"):
                num += 1
    print(num)