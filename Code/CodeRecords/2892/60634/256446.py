temp = input().split(" ")

begin = int(temp[0])
end = int(temp[1])


result = [0 for x in range(10)]
if begin == 0:
    #result[0] += 1
    begin += 1

while begin <= end:
    div = begin
    rem = 0
    while div != 0:
        rem = div%10
        div = int(div/10)
        result[rem] += 1
    begin += 1

i = 0
while i < 10:
    print(result[i],end = "")
    if i != 9:
        print(end = " ")
    i += 1
