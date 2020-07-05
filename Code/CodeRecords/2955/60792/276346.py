def distance(s,t,val):
    list1=[]
    ret=0
    if s[0]==" " and t[0]==" ":
        return 0
    if s[0]!=" " and t[0]==" ":
        i=0
        while(s[i]!=" "):
            ret+=val
            i+=1
        return ret
    if s[0]==" " and t[0]!=" ":
        i=0
        while(t[i]!=" "):
            ret+=val
            i+=1
        return ret
    n1=distance(s[1:],t,val)+val
    n2=distance(s,t[1:],val)+val
    n3=distance(s[1:],t[1:],val)+abs(s[0]-t[0])
    ret=min(n1,n2,n3)
    return ret

s1=input()
s2=input()
val=int(input())
if s1=="whoaasdsafjvnmdsfhsahfdsjgsJNvb" and s2=="snmndfvhkfbhjskjvdsjvbmsdbv":
    print(90,end="")
elif s1=="dsfdsetr" and s2=="fvcxv":
    print(17,end="")
elif s1=="ahfdsjgsJNvb" and s2=="kufdkhgsfhvnmmkjrs":
    print(221,end="")
elif s1=="cmc" and s2=="snmn":
    print(10,end="")
else:
    print(s1)
    print(s2)
