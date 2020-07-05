def sort_5_exist(k,t,list=[]):
    for i in range(1,k+1):
        for j in range(0,len(list)-i):
            if abs(int(list[j+i])-int(list[j]))<= t :
                return "true"
    return "false"
if __name__=='__main__':
    s = input()
    co = 0
    co_d = 0
    for i in range(len(s)):
        if s[i]==']':
            co = i
            break
    list = eval(s[7:co+1])
    for i in range(co+2,len(s)):
        if s[i]==',':
            co_d = i
            break
    k = int(s[(co+7):co_d])
    t = int((s[(co_d+6):]))
    print(sort_5_exist(k,t,list))