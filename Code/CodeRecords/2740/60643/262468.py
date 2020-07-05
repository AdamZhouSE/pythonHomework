timePoints=input()
#timePoints为list
st=set()#使用集合进行操作
for i in timePoints:
    temp=int(i[:2])*60+int(i[3:])
    if temp not in st:#这里也可以去重
        st.add(temp)
st=sorted(st)
st.append(st[0]+1440)#00:02和23:56只差几分钟
res=min(st[i+1]-st[i] for i in range(len(st)-1))
print(res)
