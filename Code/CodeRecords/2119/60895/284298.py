s=input().split(',')
north=int(s[0])
west=int(s[1])
south=int(s[2])
east=int(s[3])
if north>=south and west<=east:
    result=True
else:
    result=False
print(result)
         