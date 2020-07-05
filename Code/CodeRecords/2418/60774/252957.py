tomatoSlice = int(input())
cheessSlice = int(input())
flag = True
for i in range(0,cheessSlice + 1):
    if(4 * i + (cheessSlice - i) * 2 == tomatoSlice):
        print([i,cheessSlice - i])
        flag = False
        break
if(flag):
    print([])