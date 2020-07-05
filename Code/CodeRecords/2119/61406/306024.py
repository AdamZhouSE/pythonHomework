def crossing(a):
    for i in range(3,len(a)):
        if a[i]>=a[i-2] and a[i-3]>=a[i-1]:
            return True
        elif i>=4 and a[i-1]==a[i-3] and a[i-4]+a[i]>=a[i-2]:
            return True
        elif i>=5 and a[i]+a[i-4]>=a[i-2] and a[i-1]+a[i-5]>=a[i-3] and a[i-2]>=a[i-4] and a[i-3]>=a[i-1]:
            return True
    return False

    
source = input().lstrip('[').rstrip(']').split(',')
for x in range(0,len(source)):
    source[x] = int(source[x])
print(crossing(source))