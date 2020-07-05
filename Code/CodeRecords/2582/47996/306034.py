def function(s1,s2):
    result1=[]
    result2=[]
    result3=[]
    result4=[]
    for i in range(len(s1)):
        result1.append(s1[i]+s2[i]+i)
        result2.append(s1[i]+s2[i]-i)
        result3.append(s1[i]-s2[i]+i)
        result4.append(s2[i]-s1[i]+i)
    result1.sort()
    result2.sort()
    result3.sort()
    result4.sort()
    return max(result1[-1]-result1[0],result2[-1]-result2[0],result3[-1]-result3[0],result4[-1]-result4[0])

str = input().split(",")
arr1 = [int(x) for x in str]
str = input().split(",")
arr2 = [int(x) for x in str]
print(function(arr1,arr2))
