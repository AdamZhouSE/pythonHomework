li = [int(x) for x in input().split(",")]
li.sort(reverse=True)
ans = 0
for i in range(len(li)):
    for j in range(len(li)):
        if i!=j:
            for k in range(0,len(li)):
                if j!=k and i!=k:
                    l = 6 - i - j - k
                    hours = li[i]*10+li[j]
                    minutes = li[k]*10+li[l]
                    if 0<=hours<24 and 0<=minutes<60:
                        ans = max(ans,hours*60+minutes)
ans = "{:02d}:{:02d}".format(ans//60,ans%60)
if ans =="00:00":
    print("")
    exit()
print(ans)