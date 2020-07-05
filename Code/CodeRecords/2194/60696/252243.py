arr = '2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97'
prime_nums = [int(i) for i in arr.split('、')]
n = int(input())
for i in range(n):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    res = []
    for j in prime_nums:
        if a <= j <= b:
            res.append(j)
        elif j > b:
            break
    for j in res:
        print(j, end=' ')
    print()