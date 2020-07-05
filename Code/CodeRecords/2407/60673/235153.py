
y, m, d = map(int,input().split('-'))
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%4 != 0:
    month[2] = 28
elif y%100==0 and y%400 != 0:
    month[2] = 28           
print (sum(month[:m])+d)
