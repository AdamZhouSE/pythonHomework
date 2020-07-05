def arrays_35_leastStr(list = []):
    list_0 = sorted(list)
    co = 0
    for i in range(len(list)):
         if list[i]!=list_0[i]:
             co += 1
    if co==2:
        print(2)
    else:print(co+1)
if __name__=='__main__':
    list = eval(input())
    arrays_35_leastStr(list)